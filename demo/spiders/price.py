import scrapy
from scrapy_splash import SplashRequest
class Price(scrapy.Spider):
    name = 'pricespider'
    allowed_domains = ['www.booking.com']
    #start_urls = ['https://www.booking.com/hotel/ca/kimbrook-lodge.en-gb.html']
    
    def start_requests(self):
        url="https://www.booking.com/hotel/ca/kimbrook-lodge.en-gb.html"        
        yield SplashRequest(url)
        
        
        
    def parse(self,response):
        s = '#rooms_table > div:nth-child(3) > div > section > div'
        print(response.css(s).getall())
        for i in response.css(s):
            price=i.css('.prco-valign-middle-helper::text').get()
        yield {'price':price}     
    
    
    
    
    
    