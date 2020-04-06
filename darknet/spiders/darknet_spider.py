# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urlparse
from darknet.items import TorItem
from scrapy.spiders import CrawlSpider



TOR_WIKI_URL = 'http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page'

class TorSpider(CrawlSpider):
    name = 'tor_spider'
    start_urls = [TOR_WIKI_URL,]
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'darknet.middlewares.TorSpiderMiddleware': 543,
        },
        'ITEM_PIPELINES': {
            'darknet.pipelines.TorPipeline': 500,
        }
    }

    def parse_start_url(self, response):
        item = TorItem()
        item['name'] = response.xpath('/html/head/title/text()').extract()[0]
        item['url'] = response.url
        item['status'] = response.status
        # item['html'] = bytes.decode(response.body)
        yield item
        for url in response.xpath('//a/@href').extract():
            if re.match(r'http:.*', url) \
            and urlparse(url).netloc != urlparse(response.url).netloc:
                if re.match(r'.*onion', url):
                    yield scrapy.Request(url, callback=self.parse_other)


    def parse_other(self, response):
        item = TorItem()
        item['name'] = response.xpath('/html/head/title/text()').extract()[0]
        item['url'] = response.url
        item['status'] = response.status
        # item['html'] = bytes.decode(response.body)
        yield item

    # def parse(self,response):
    #     print(response.body)
        

        

   
