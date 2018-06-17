# -*- coding: utf-8 -*-
import scrapy



class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['chinaz.com']
    # allowed_domains = ['163.com']
    # allowed_domains = ['zhihu.com']
    # allowed_domains = ['sina.com']
    # allowed_domains = ['meituan.com']
    # start_urls = ['http://chinaz.com/']

    def start_requests(self):

        for _ in range(20):
            url  = 'http://ip.chinaz.com/getip.aspx'
            # url = 'http://www.zhihu.com'
            # url = 'http://www.163.com'
            # url = 'http://www.sina.com'
            # url = 'https://km.meituan.com/'
            yield scrapy.Request(url=url,callback=self.parse, dont_filter=True)

    def parse(self,response):
        print(response.body.decode('utf-8'))
        # print(response.css('.detail-title-wrapper ::text').extract())
        # print(response.headers)


