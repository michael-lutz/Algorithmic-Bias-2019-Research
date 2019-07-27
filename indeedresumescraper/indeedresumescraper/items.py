# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data -> Temporary containers (items) -> Storing in database

import scrapy


class IndeedresumescraperItem(scrapy.Item):
    # define the fields for your item here like:
    jobsearch = scrapy.Field()
    candidatetitle = scrapy.Field()
    rank = scrapy.Field()
    resume = scrapy.Field()
