import scrapy 
import json

class LocationVac_links_Spider(scrapy.Spider):
    name = "LocationVac_links"
    start_urls=["https://www.mubawab.ma/fr/sc/appartements-vacational"]

    def parse(self, response):
        for property in response.css('li.listingBox.w100'):
            yield {
                'Property_link': property.css('::attr(linkref)').get()
            }
        next_page=response.css('div.paginationDots.sMargTop.centered a::attr(href)')[-1].get()
        if next_page is not None:
            yield response.follow(url= next_page, callback= self.parse)
class LocationVac_data_Spider(scrapy.Spider):
    name = "LocationVac_data"
    with open('5-locationVac_links.json', 'r') as f:
        data= json.load(f)
    start_urls=[item['Property_link'] for item in data]

    def parse(self, response):
        yield {
            'Property link': response.url,
            'title': response.css("div.mainInfoProp > h1::text").get().strip(),
            'price': response.css("div.row.disFlex > div > h3.orangeTit::text").get().strip().replace("\xa0",""),
            'localisation': response.css("div.mainInfoProp > h3.greyTit::text").get().replace("\n","").replace("\t",""),
            'main_image': response.css("img.currentImgSldr.w100.updatable::attr(src)").extract_first(),
            'tags': response.css("div.catNav >span.tagProp::text").extract(),
            'Description': response.css("div.blockProp > p::text").extract(),
            'Caracteristiques': response.css("div.row.rowIcons.adFeatures.inBlock.w100 > ul > li > div > div > span::text").extract(),
            'exact_local' : response.css("div.blockProp.mapBlockProp > script::text").extract_first().strip(),
            'agence_website': response.css("div.agency-info > p.link > a::attr(href)").extract_first(),
            'agence_name': response.css("div.agency-info > p.link > a::text").extract_first(),
            'agence_logo':response.css("div.agency-info > a > img::attr(src)").extract_first(),
        }