# CSS Selectors
<p> After Visiting <a href="https://www.mubawab.ma/">Moubawab Website</a> We select <a href="https://www.mubawab.ma/fr/listing-promotion">Immobilier Neuf </a> </p>

next_page= response.css('a.arrowDot::attr(href)').get()
next_page2=response.css('div.paginationDots.sMargTop.centered a::attr(href)')[-1].get()

all_properties= response.css('li.promotionListing.listingBox.w100')
all_properties_link = response.css('li.promotionListing.listingBox.w100::attr(linkref)')


