import scrapy

class Ebay_spider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ["https://www.ebay.com"]
    start_urls = ['https://www.ebay.com/sch/i.html?_nkw=antique+book&_sop=12&_pgn=6&rt=nc']

    def parse(self, response):
        element = response.css(".s-item__info.clearfix")
        for items in element[1:]:
            name = items.css("h3.s-item__title::text").get()
            price = items.css(".s-item__price::text").get()
            yield {
                "name": name,
                "price": price
            }


        next_page = response.css("a.pagination__next.icon-link::attr(href)").get()
        # import pdb; pdb.set_trace()
        if next_page:
            yield response.follow(next_page, callback=self.parse)






