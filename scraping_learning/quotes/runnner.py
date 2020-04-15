import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes.spiders.quote import QuoteSpider

# If you have a problem to import a local package in Pycharm use follow these steps:
# Preferences -> Project -> Project structure
# put the desired folder as source


process = CrawlerProcess(settings=get_project_settings())
process.crawl(QuoteSpider)
process.start()
