# -*- coding: utf-8-*-
from setuptools import setup
setup(
    name='scrapy-sqs',
    version='0.0.3',
    description='SQS Plug-in for Scrapy',
    author='GabrielB',
    author_email='gbalensiefer@gmail.com',
    license='MIT',
    url='https://github.com/gabrielb/scrapy-sqs',
    install_requires=['Scrapy>=1.0', 'boto3'],
    packages=['scrapy_sqs']
)
