import scrapy

class Moubawab_Spider(scrapy.Spider):
    name = "moubawab_spider"
    start_urls=[" https://www.mubawab.ma/fr/listing-promotion"]

    def parse(self, response):
        for property in response.css('li.promotionListing.listingBox.w100'):
            yield {
                'Property_link': property.css('::attr(linkref)').get()
            }
        
        # next_page= response.css('a.arrowDot::attr(href)').get()
        next_page2=response.css('div.paginationDots.sMargTop.centered a::attr(href)')[-1].get()

        print(f'the link of the next page is : {next_page2}')
        if next_page2 is not None:
            # next_page_url = response.urljoin(next_page)
            yield response.follow(url= next_page2, callback= self.parse)
            # yield scrapy.follow(url= next_page, callback= self.parse)
