# CSS Selectors


## Immobilier Neuf links 

<p> After Visiting <a href="https://www.mubawab.ma/">Moubawab Website</a> We select <a href="https://www.mubawab.ma/fr/listing-promotion">Immobilier Neuf </a> </p>

next_page= response.css('a.arrowDot::attr(href)').get()
next_page2=response.css('div.paginationDots.sMargTop.centered a::attr(href)')[-1].get()

all_properties= response.css('li.promotionListing.listingBox.w100')
all_properties_link = response.css('li.promotionListing.listingBox.w100::attr(linkref)')

## Immobilier Neuf data 
Name = response.css("div.promotionInfoBox.col-5 > h1::text").extract_first().strip()
location= response.css("div.promotionInfoBox.col-5 > span::text").extract()[1].strip()
price = response.css("div.promotionInfoBox.col-3 > h2::text").extract_first().replace('\n', '').replace('\t', '').replace('\xa0','').replace('de','de ')

try:
    video_link, virtual_visit = response.css("div.descrBlockProp.noTop > iframe::attr(src)").extract()
except:
    video_link=response.css("div.descrBlockProp.noTop > iframe::attr(src)").extract_first()


Description= response.css("div.descrBlockProp.descHolder > p ::text ").extract() # list of texts you should loop throught it and stripe each.
 
main_image=response.css("img.currentImgSldr.w100 ::attr(src)").extract_first()

exact_localisation=response.css("div.blockProp.mapBlockProp > script::text").extract_first().replace('\n', '').replace('\t', '')
def extract_text(string, start_str, end_str):
    """
    Extracts the text from a string between the start_str and end_str substrings.
    Returns an empty string if either substring is not found in the string.
    """
    start_index = string.find(start_str)
    if start_index == -1:
        return ""
    end_index = string.find(end_str, start_index + len(start_str))
    if end_index == -1:
        return ""
    return string[start_index + len(start_str):end_index]

Project_name = response.css("div.agencyBigContent > h2::text").extract_first()
logo= response.css("div.logoAgencyBox > img::attr(src)").extract_first()
project_description= response.css("p.agencyText::text").extract_first().strip().replace('\n', '').replace('\t', '').replace('\r', '')
phone_number=response.css("span.marginContact.dirLtr::text").extract_first().strip()
website=response.css("a.agencyLink::attr(href)").extract()[1]

## Vente links
Similiar to the Immo_neuf_linksspider Spider

## Vente data

title= response.css("div.mainInfoProp > h1::text").get().strip()
price= response.css("div.row.disFlex > div > h3.orangeTit::text").get().strip().replace("\xa0","")
localisation= response.css("div.mainInfoProp > h3.greyTit::text").get().replace("\n","").replace("\t","")
main_image= response.css("img.currentImgSldr.w100.updatable::attr(src)").extract_first()
tags= response.css("div.catNav >span.tagProp::text").extract()
Description = response.css("div.blockProp > p::text").extract()
Caracteristiques= response.css("div.row.rowIcons.adFeatures.inBlock.w100 > ul > li > div > div > span::text").extract() 
exact_local= response.css("div.blockProp.mapBlockProp > script::text").extract_first().strip()
agence_website= response.css("div.agency-info > p.link > a::attr(href)").extract_first()
agence_logo= response.css("div.agency-info > a > img::attr(src)").extract_first()
agence_name= response.css("div.agency-info > p.link > a::text").extract_first()

## Agencies Data & Items

agency_name= response.css("div.agencyBigContent.col-7 > h1::text").extract_first()
agency_adresse= response.css("div.agencyBigContent.col-7 > span::text").extract_first()
phone_number= response.css("div.contactLegend > a::attr(href)").extract_first()
website_if_exists= response.css("div.contactLegend > a::attr(href)").extract()[-1] # if len()>1 website exists else not exists
number_of_properties= response.css("div.col-12 > p::text").extract_first().replace("\t","").replace("\n","")

next_page= response.css("div.paginationDots.sMargTop.centered > a.arrowDot::attr(href)").extract_first()
property_link= response.css("div.contnr1100.mainContnr > ul > li > div.contentBox.col-8 > h2.listingTit > a::attr(href)").extract()
property_title= response.css("div.contnr1100.mainContnr > ul > li > div.contentBox.col-8 > h2.listingTit > a::text").extract()
property_price= response.css("div.contnr1100.mainContnr > ul > li > div.photoBox.col-4.floatR.emptyCol > div > span::text").extract()