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
project_description= response.css("p.agencyText::text").extract_first().strip()
phone number=response.css("span.marginContact.dirLtr::text").extract_first().strip()
website=response.css("a.agencyLink::attr(href)").extract()[1]

