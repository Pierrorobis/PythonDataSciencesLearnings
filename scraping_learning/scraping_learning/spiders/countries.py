# -*- coding: utf-8 -*-
import scrapy

class CountriesSpider(scrapy.Spider):

    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # title = response.xpath("//h1/text()").get()
        # In oder to get all output at once and return it as whole:
        # countries_names = response.xpath("//table/descendant::a/text()").getall()
        # countries_links = response.xpath("//table/descendant::a/@href").getall()
        countries = response.xpath("//table/descendant::a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_country, meta={'name': name})

    def parse_country(self, response):
        country_data = response.xpath("(//div[@class='table-responsive'])[1]/descendant::tbody/tr")
        for data_per_year in country_data:
            year = data_per_year.xpath("./td[1]/text()").get()
            population = data_per_year.xpath("./td/strong/text()").get()

            yield {
                "name": response.meta["name"],
                "year": year,
                "population": population
            }
