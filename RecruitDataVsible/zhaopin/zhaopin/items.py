# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    number = scrapy.Field()
    job = scrapy.Field()
    post_type = scrapy.Field()
    city = scrapy.Field()
    job_place = scrapy.Field()
    job_experience = scrapy.Field()
    education = scrapy.Field()
    min_wage = scrapy.Field()
    max_wage = scrapy.Field()
    job_duty = scrapy.Field()
    job_benefits = scrapy.Field()
    update_time = scrapy.Field()

    company = scrapy.Field()
    logo = scrapy.Field()
    website = scrapy.Field()
    industry = scrapy.Field()
    scale= scrapy.Field()

