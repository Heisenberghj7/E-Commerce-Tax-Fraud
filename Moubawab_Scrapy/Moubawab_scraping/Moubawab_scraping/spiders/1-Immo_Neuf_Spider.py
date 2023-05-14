import scrapy
import json

class Immobilier_Neuf_links_spider(scrapy.Spider):
    name = "Immobilier_Neuf_links"
    start_urls=["https://www.mubawab.ma/fr/listing-promotion"]

    def parse(self, response):
        for property in response.css('li.promotionListing.listingBox.w100'):
            yield {
                'Property_link': property.css('::attr(linkref)').get()
            }
        
        #next_page= response.css('a.arrowDot::attr(href)').get()
        next_page2=response.css('div.paginationDots.sMargTop.centered a::attr(href)')[-1].get()
        print(f'the link of the next page is : {next_page2}')
        if next_page2 is not None:
            # next_page_url = response.urljoin(next_page)
            yield response.follow(url= next_page2, callback= self.parse)
            # yield scrapy.follow(url= next_page, callback= self.parse)

class Immobilier_Neuf_data_spider(scrapy.Spider):
    name = "Immobilier_Neuf_data"

    with open('1-Immo_Neuf_links.json', 'r') as f:
        data= json.load(f)
    
    start_urls=[item['Property_link'] for item in data]

    def parse(self, response):
        try:
            video_link, virtual_visit = response.css("div.descrBlockProp.noTop > iframe::attr(src)").extract()
        except:
             video_link=response.css("div.descrBlockProp.noTop > iframe::attr(src)").extract_first()
             virtual_visit=''
        yield {
            'Name': response.css("div.promotionInfoBox.col-5 > h1::text").extract_first().strip(),
            'location':response.css("div.promotionInfoBox.col-5 > span::text").extract()[1].strip(),
            'Exact_localisation': response.css("div.blockProp.mapBlockProp > script::text").extract_first().replace('\n', '').replace('\t', ''),
            'price':response.css("div.promotionInfoBox.col-3 > h2::text").extract_first().replace('\n', '').replace('\t', '').replace('\xa0','').replace('de','de '),
            'Description':response.css("div.descrBlockProp.descHolder > p ::text ").extract(),
            'video_link':video_link,
            'virtual_visit':virtual_visit,
            'main_image':response.css("img.currentImgSldr.w100 ::attr(src)").extract_first(),
            'project_name': response.css("div.agencyBigContent > h2::text").extract_first(),
            'logo': response.css("div.logoAgencyBox > img::attr(src)").extract_first(),
            'project_description':response.css("p.agencyText::text").extract_first().strip().replace('\n', '').replace('\t', '').replace('\r', ''),
            'phone_number':response.css("span.marginContact.dirLtr::text").extract_first().strip(),
            'website':response.css("a.agencyLink::attr(href)").extract()[1]

        }