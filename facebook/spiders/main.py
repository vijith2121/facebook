import scrapy
# from facebook.items import Product
from lxml import html

class FacebookSpider(scrapy.Spider):
    name = "facebook"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)
