# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name::text').extract()[0].strip().split()[0]
        keyList = stockInfo.css('dt::text').extract()
        valueList = stockInfo.css('dd::text').extract()
        for i in range(len(keyList)):
            key = keyList[i].strip()
            value = valueList[i].strip()
            infoDict[key] = value
        infoDict['股票名称'] = name
        yield infoDict
