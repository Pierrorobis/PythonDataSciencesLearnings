# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from urllib.parse import urljoin
import logging


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com'] # VERY VERY IMPORTANT, OTHERWISE IT WON'T WORK FOR THE NEXT PAGES
    start_urls = ['http://quotes.toscrape.com/js/']

    # The following script is not used here, but it shows how to scroll, and click a button using javascript
    # based on the button content !
    script = """
    function main(splash, args)
      splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15")
      assert(splash:go(args.url))
      assert(splash:wait(1))
      
      splash.scroll_position = {y=1800}
      splash:wait(1)
      
      local get_dimensions = splash:jsfunc([[
        function () {
          var aTags = document.getElementsByTagName("a");
          var searchText = "Next";
          var found;
    
          for (var i = 0; i < aTags.length; i++) {
            if (aTags[i].textContent.includes(searchText)) {
              found = aTags[i];
            break;
                }
          }
        // Handle case with empty found var
            var rect = found.getClientRects()[0];
          return {"x": rect.left, "y": rect.top}
        }
        ]])
      
      local dimensions = get_dimensions()
      
      splash:mouse_click(dimensions.x+10, dimensions.y+10)
      -- Wait split second to allow event to propagate.
      splash:wait(1)
      return {
        dim = dimensions,
        html = splash:png()
        }
    end
    """
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_item, args={'wait': 0.5})

    def parse_item(self, response):
        body = response.body
        quotes_selectors = scrapy.Selector(text=body)
        quotes = quotes_selectors.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                'quote': quote.xpath("./span[@class='text']/text()").get(),
                'author': quote.xpath("./span/small[@class='author']/text()").get(),
                'tags': quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall()
            }

        next = response.xpath("//nav/ul/li[@class='next']/a/@href").get()
        if next:
            logging.info(urljoin(response.url, next))
            # Following line does not work
            yield SplashRequest(url=urljoin(response.url, next), callback=self.parse_item, args={'wait': 0.5})
