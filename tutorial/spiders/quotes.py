# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem, article

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['en.wikipedia.org']
    #start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Former_featured_articles']
    start_urls = ['https://en.wikipedia.org/wiki/wikipedia:Featured_articles']


#    ESTA ES LA PRUEBA DE PRENSALIBRE PARA JALAR PARRAFOS
    def parse(self, response):

        host = self.allowed_domains[0]
        for link in response.css(".featured_article_metadata > a"):
            link = f"{link.attrib.get('href')}"
            title = link
            #print(title)
            yield response.follow(link,callback=self.parse_detail,meta={'link': link, 'title':title})

    def parse_detail(self,response):
        items = TutorialItem()
        item  = article()
        items["link"] = response.meta["link"]
        item["title"] = response.meta["title"]
        item["parrafo"] = list()

        for text in response.css(".mw-parser-output > p::text").extract():
            item["parrafo"].append(text)

        items["body"] = item
        return items


#    ESTA ES LA PRUEBA DE wikipedia para jalar parrafos
#    def parse(self, response):
#
#        host = self.allowed_domains[0]
#        for link in response.css(".featured_article_metadata > a"):
#            link = f"{link.attrib.get('href')}"
#            title = link
#            #print(title)
#            yield response.follow(link,callback=self.parse_detail,meta={'link': link, 'title':title})

#    def parse_detail(self,response):
#        items = TutorialItem()
#        item  = article()
#        #print("AQUI")
#        #print(response.meta["link"])
#        items["link"] = response.meta["link"]
#        item["title"] = response.meta["title"]
#        item["parrafo"] = list()

#        for text in response.css(".mw-parser-output > p::text").extract():
#            item["parrafo"].append(text)

#        items["body"] = item
#        return items

#    ESTA ES LA PRUEBA DE WIKIPEDIA
#    def parse(self, response):
#        host = self.allowed_domains[0]
#        for link in response.css(".featured_article_metadata > a"):
#            yield TutorialItem(
#                title = link.attrib.get("title"),
#                link = f"https://{host}{link.attrib.get('href')}"
#            )