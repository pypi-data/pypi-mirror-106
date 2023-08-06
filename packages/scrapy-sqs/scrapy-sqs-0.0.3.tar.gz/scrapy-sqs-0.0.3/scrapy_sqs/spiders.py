from scrapy import signals
from scrapy.exceptions import DontCloseSpider
from scrapy.spiders import Spider, CrawlSpider
from collections import Iterable
import time

from . import connection


class SQSMixin(object):
    """Mixin class to implement reading urls from a sqs queue."""
    sqs_queue_url = None
    sqs_queue_name = None
    sqs_batch_size = None

    # SQS client placeholder.
    sqs = None
    queue = None

    # Idle start time
    spider_idle_start_time = int(time.time())

    def start_requests(self):
        """Returns a batch of start requests from sqs."""
        return self.next_requests()

    def setup_sqs(self, crawler=None):
        """Setup sqs connection and idle signal.

        This should be called after the spider has set its crawler object.
        """
        if self.sqs is not None:
            return

        if crawler is None:
            # We allow optional crawler argument to keep backwards
            # compatibility.
            # XXX: Raise a deprecation warning.
            crawler = getattr(self, 'crawler', None)

        if crawler is None:
            raise ValueError("crawler is required")

        settings = crawler.settings

        if self.sqs_queue_url is None:
            self.sqs_queue_url = settings.get('SQS_QUEUE_URL')

        if self.sqs_queue_name is None:
            self.sqs_queue_name = settings.get('SQS_QUEUE_NAME')

        if not self.sqs_queue_url and not self.sqs_queue_name:
            raise ValueError("Either sqs_queue_url or sqs_queue_name is required.")

        if self.sqs_batch_size is None:
            self.sqs_batch_size = settings.getint('CONCURRENT_REQUESTS')

        try:
            self.sqs_batch_size = int(self.sqs_batch_size)
        except (TypeError, ValueError):
            raise ValueError("sqs_batch_size must be an integer")

        if self.sqs_batch_size > 10:
            raise ValueError("sqs_batch_size must be between 1 and 10. Check CONCURRENT_REQUESTS value.")

        self.logger.info("Reading start URLs from sqs queue %(sqs_queue_url) %(sqs_queue_name)", self.__dict__)

        self.sqs = connection.from_settings(crawler.settings)

        if self.sqs_queue_url:
            self.queue = self.sqs.Queue(self.sqs_queue_url)
        else:
            self.queue = self.sqs.get_queue_by_name(QueueName=self.sqs_queue_name)

        # The idle signal is called when the spider has no requests left,
        # that's when we will schedule new requests from sqs queue
        crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)

    def next_requests(self):
        """Returns a request to be scheduled or none."""
        # XXX: Do we need to use a timeout here?
        found = 0
        datas = self.fetch_data(self.sqs_batch_size)
        for data in datas:
            reqs = self.make_request_from_data(data)
            if isinstance(reqs, Iterable):
                for req in reqs:
                    yield req
                    # XXX: should be here?
                    found += 1
                    self.logger.info(f'start req url:{req.url}')
            elif reqs:
                yield reqs
                found += 1
            else:
                self.logger.debug("Request not made from data: %r", data)
            data.delete()
        if found:
            self.logger.debug("Read %s requests from '%s'", found, self.sqs_queue_name)

    def fetch_data(self, batch_size):
        return self.queue.receive_messages(MaxNumberOfMessages=batch_size)

    def make_request_from_data(self, data):
        """Returns a Request instance from message coming from SQS.

        By default, ``data`` is an message with url. You can override this method to
        provide your own message decoding.

        """
        url = data.body
        return self.make_requests_from_url(url)

    def schedule_next_requests(self):
        """Schedules a request if available"""
        # TODO: While there is capacity, schedule a batch of sqs requests.
        for req in self.next_requests():
            self.crawler.engine.crawl(req, spider=self)

    def spider_idle(self):
        """
        Schedules a request if available, otherwise waits.
        or close spider when waiting seconds > MAX_IDLE_TIME_BEFORE_CLOSE.
        MAX_IDLE_TIME_BEFORE_CLOSE will not affect SCHEDULER_IDLE_BEFORE_CLOSE.
        """
        if self.queue is not None:
            self.spider_idle_start_time = int(time.time())

        self.schedule_next_requests()

        max_idle_time = self.settings.getint("MAX_IDLE_TIME_BEFORE_CLOSE")
        idle_time = int(time.time()) - self.spider_idle_start_time
        if max_idle_time != 0 and idle_time >= max_idle_time:
            return
        raise DontCloseSpider


class SQSSpider(SQSMixin, Spider):
    """Spider that reads urls from sqs queue when idle.

    Attributes
    ----------
    sqs_queue_url : str (default: SQS_QUEUE_URL)
        SQS queue url where to fetch start URLs from. Either sqs_queue_url or sqs_queue_name is required.
    sqs_queue_name : str (default: SQS_QUEUE_NAME)
        SQS queue name where to fetch start URLs from. Either sqs_queue_url or sqs_queue_name is required.
    sqs_batch_size : int (default: CONCURRENT_REQUESTS)
        Number of messages to fetch from sqs on each attempt.

    Settings
    --------
    SQS_QUEUE_URL : str
        Default sqs queue url where to fetch start URLs from.
    SQS_QUEUE_NAME : str
        Default sqs queue name where to fetch start URLs from.

    """

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(SQSSpider, self).from_crawler(crawler, *args, **kwargs)
        obj.setup_sqs(crawler)
        return obj


class SQSCrawlSpider(SQSMixin, CrawlSpider):
    """Spider that reads urls from sqs queue when idle.

    Attributes
    ----------
    sqs_queue_url : str (default: SQS_QUEUE_URL)
        SQS queue url where to fetch start URLs from. Either sqs_queue_url or sqs_queue_name is required.
    sqs_queue_name : str (default: SQS_QUEUE_NAME)
        SQS queue name where to fetch start URLs from. Either sqs_queue_url or sqs_queue_name is required.
    sqs_batch_size : int (default: CONCURRENT_REQUESTS)
        Number of messages to fetch from sqs on each attempt.

    Settings
    --------
    SQS_QUEUE_URL : str
        Default sqs queue url where to fetch start URLs from.
    SQS_QUEUE_NAME : str
        Default sqs queue name where to fetch start URLs from.

    """

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(SQSCrawlSpider, self).from_crawler(crawler, *args, **kwargs)
        obj.setup_sqs(crawler)
        return obj