import scrapy 
import json

class Agencies_Spider(scrapy.Spider):
    name = "Agencies_spider"
    with open('C:\\Users\\HAJJARI\\Desktop\\AI\\13-GithubRepos\\E-Commerce-Tax-Fraud\\Moubawab_Scrapy\\Moubawab_scraping\\Moubawab_scraping\\spiders\\2-vente_data.json', 'r',encoding="utf8") as f:
        data= json.load(f)
    start_urls=list(set([item['agence_website'] for item in data]))
    def parse(self, response):
        try:
            yield {
                'agency_name': response.css("div.agencyBigContent.col-7 > h1::text").extract_first(),
                'agency_adresse': response.css("div.agencyBigContent.col-7 > span::text").extract_first(),
                'phone_number' : response.css("div.contactLegend > a::attr(href)").extract_first(),
                'website_if_exists': response.css("div.contactLegend > a::attr(href)").extract(),
                'number_of_properties': response.css("div.col-12 > p::text").extract_first().replace("\t","").replace("\n",""),
                'property_link':response.css("div.contnr1100.mainContnr > ul > li > div.contentBox.col-8 > h2.listingTit > a::attr(href)").extract(),
                'property_title': response.css("div.contnr1100.mainContnr > ul > li > div.contentBox.col-8 > h2.listingTit > a::text").extract(),
                'property_price': response.css("div.contnr1100.mainContnr > ul > li > div.photoBox.col-4.floatR.emptyCol > div > span::text").extract()
                
            }
            next_page= response.css("div.paginationDots.sMargTop.centered > a.arrowDot::attr(href)").extract_first()
            if next_page is not None:
                yield response.follow(url= next_page, callback= self.parse)
        except: 
            pass