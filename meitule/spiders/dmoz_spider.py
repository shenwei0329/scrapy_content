# -*- coding: utf-8 -*-
#
# 2016.11.22 @chengdu by shenwei.
# - 精确定位page
#

from scrapy import Spider
from scrapy.selector import Selector


class DmozSpider(Spider):

    name = "dmoz"
    allowed_domains = ["baike.baidu.com"]
    start_urls = []
    _url = "https://baike.baidu.com/item/"
    for _y in range(1600, 2020):
        start_urls.append(_url + "%04d年" % _y)

    def save(self, info):
        f = open("date.txt", "a")
        f.write(info.encode("utf-8"))
        f.write("\n")
        f.close()

    def parse(self, response):
        sel = Selector(response)
        """获取年份"""
        year = sel.xpath('//div[@class="main-content"]/dl/dd/h1/text()').extract()[0].split(u"：")[0]
        print year
        """收集目标：有效的信息条目"""
        main_content = sel.xpath('//div[@class="main-content"]/div[@class="para"] | '
                                 '//div[@class="main-content"]/div[@class="para-title level-2"]')
        pp = ""
        for _content in main_content:
            """按顺序获取信息"""
            """1、信息分类"""
            _pp = _content.xpath('./h2/text()').extract()
            if len(_pp) > 0:
                pp = _pp[0]
            """2、获取该分类下的信息"""
            info = _content.xpath('./text() | a[@target="_blank"][@href]/text()').extract()
            if len(info) > 0 and u"月" not in info[0] and u"日" not in info[0]:
                continue
            _str = year
            _str += "^"
            _str += pp
            _str += "^"
            for _info in info:
                if len(_info) == 0:
                    continue
                _str += _info
            _str = _str.replace("\n", "").replace("\r", "").replace(" ", "").replace(u"：", "^")
            if _str[-1] != "^":
                """存储有实质内容的信息"""
                self.save(_str)

#
# Eof
#
