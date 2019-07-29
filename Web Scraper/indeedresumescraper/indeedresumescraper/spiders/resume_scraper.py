import scrapy

from scrapy_splash import SplashRequest
from ..items import IndeedresumescraperItem


class QuoteSpider(scrapy.Spider):
    name = 'candidates'
    start_urls = [
        'https://resumes.indeed.com/search?q=data+science&l=&searchFields=jt'
    ]

    def start_requests(self):
        for url in self.start_urls:
                yield SplashRequest(url, self.parse, endpoint='render.html', args={"wait": 3})

    def parse(self, response):

        items = IndeedresumescraperItem()

        for candidates in response.css("div.rezemp-ResumeSearchCard-contents"):
            candidatetitle = candidates.css('.rezemp-u-h4::text').extract()

            items['candidatetitle'] = candidatetitle

            yield items
