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
 
Images=
exact_localisation=

Project_name =
logo=
project_description=
phone number=
website=

