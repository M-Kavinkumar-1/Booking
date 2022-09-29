# -*- coding: utf-8 -*-
from tracemalloc import start
import scrapy
import random

#import logging

class AaidSpider(scrapy.Spider):
    name = 'a'
    # start_urls = ['http://x.com/']
   
    
    def parse(self, response):
        self.logger.info('test5')
        print(response, response.body)
        pass
    def start_requests(self):

        url = "https://www.booking.com/hotel/ca/kimbrook-lodge.en-gb.html"+ "?dummy=" + str(random.random())
        cookies = {
    '_pxhd': '9ije37phpJKAjLdTaWRO-lTbP%2FbQEVG-rZLlYKUd6NyCI2sQBlCX46MWmUwhnSuiGbzuOcRsPoHBkJfgl4jQyQ%3D%3D%3ADKxEp3jEeypBXeHpCfyz3GIoHxsLSlEoKLwZ%2FbIGfXH9Ye1io%2FRbBxMpvnUeQ54GVcdK3FzYBu5q33fbpBhFHUvvU1qBEjl%2FkFr0Cz3A33s%3D',
    'cors_js': '1',
    'bkng_frontend_sese_exp': '1',
    'BJS': '-',
    '_gid': 'GA1.2.1184023220.1664420813',
    'bkng_sso_session': 'e30',
    'OptanonConsent': 'implicitConsentCountry=nonGDPR&implicitConsentDate=1664420813100',
    'pxcts': 'c502e785-3fa3-11ed-84ff-686879646e74',
    '_pxvid': 'c2207f96-3fa3-11ed-99c6-65435468596c',
    'bkng_sso_ses': 'eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6InFvNXFBcVk5N2NoOWZST1hsbkFQelZPeEFOeDNkMmtLYk02bGs5WXdWNmcifV19',
    '_px_f394gi7Fvmc43dfg_user_id': 'YzYzNDc4NjEtM2ZhMy0xMWVkLTlhY2YtY2JiMzkwYzBlOWI1',
    '_gcl_au': '1.1.733817114.1664420816',
    'bkng_prue': '1',
    '_ga_FPD6YLJCJ7': 'GS1.1.1664420816.1.0.1664420816.0.0.0',
    '_ga': 'GA1.1.331326721.1664420813',
    '_scid': '14cf6a01-9758-4c96-9214-09f01fb9b09a',
    '_sctr': '1|1664389800000',
    '_pin_unauth': 'dWlkPVpUTTFPR05oTUdNdE56SmpPQzAwTTJNNUxXRmxObVl0TkRrNU1HSm1NRGc1TUdVMA',
    '_uetsid': 'c6ff02703fa311ed859c15a4607c71a4',
    '_uetvid': 'c6ff2b303fa311ed881da1bdc6d90b0e',
    'has_preloaded': '1',
    'qr_is_sr': 'fast-click',
    '11_srd': '%7B%22features%22%3A%5B%7B%22id%22%3A5%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D',
    'g_state': '{"i_p":1664433769185,"i_l":1}',
    '_px3': 'cb4d09c8068c29502a8ad23ec7cc98d73253e998596489172d9e8e65b21195a0:4sbBK8qybTc5o2hKuTJKvTqq9bV7KU4s4youQBw2FQ/VnK/m9tm7VJebwz4J9pVu0sFbJMaMooFqmdNEOj2INw==:1000:WV04La49SMXfu9WAlj9rD9aWqZ1HzmcrBR1xWjgVHlUWOsaAmgAK3VJ67pjRykvce+sUJaQ997UQuZ/8j4rYk4sFegAb3YnjHN0zJCugS6uPf2JYtS40sQrrxZXXeHlkGu8UWFYoTi5SGIplU1ncRpBLtl4ru3/jnkXuF5ZW8vxy5zrGL/HvjZt7GdQS4QH77RfbbFgOHkSMHp7nsSMCbA==',
    '_pxde': '201956c7a313ebe8f6238dacc869694a1170fded40d2e9b626b37cac020aa499:eyJ0aW1lc3RhbXAiOjE2NjQ0MjY1ODY1ODYsImZfa2IiOjAsImlwY19pZCI6W119',
    'arp_scroll_position': '1500',
    'bkng': '11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbbmD9q%2B5pe3VFUNFW2AZvfBz%2By%2Fmxj4AlqCO0nfOWSCNt37%2Bwxuqro7ry8NQ0g16Tzn99XctWciZAq2UfA4tWeTsVUIZg6wH3UAAurZYOLgQWbN2O8Vc6Iqs5Ug9rnc5cl2BTQ9TxjwmTWxN6J04QapitKIuobqKI1vA9ZOuforA%3D',
    'lastSeen': '0',
}

        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_pxhd=9ije37phpJKAjLdTaWRO-lTbP%2FbQEVG-rZLlYKUd6NyCI2sQBlCX46MWmUwhnSuiGbzuOcRsPoHBkJfgl4jQyQ%3D%3D%3ADKxEp3jEeypBXeHpCfyz3GIoHxsLSlEoKLwZ%2FbIGfXH9Ye1io%2FRbBxMpvnUeQ54GVcdK3FzYBu5q33fbpBhFHUvvU1qBEjl%2FkFr0Cz3A33s%3D; cors_js=1; bkng_frontend_sese_exp=1; BJS=-; _gid=GA1.2.1184023220.1664420813; bkng_sso_session=e30; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1664420813100; pxcts=c502e785-3fa3-11ed-84ff-686879646e74; _pxvid=c2207f96-3fa3-11ed-99c6-65435468596c; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6InFvNXFBcVk5N2NoOWZST1hsbkFQelZPeEFOeDNkMmtLYk02bGs5WXdWNmcifV19; _px_f394gi7Fvmc43dfg_user_id=YzYzNDc4NjEtM2ZhMy0xMWVkLTlhY2YtY2JiMzkwYzBlOWI1; _gcl_au=1.1.733817114.1664420816; bkng_prue=1; _ga_FPD6YLJCJ7=GS1.1.1664420816.1.0.1664420816.0.0.0; _ga=GA1.1.331326721.1664420813; _scid=14cf6a01-9758-4c96-9214-09f01fb9b09a; _sctr=1|1664389800000; _pin_unauth=dWlkPVpUTTFPR05oTUdNdE56SmpPQzAwTTJNNUxXRmxObVl0TkRrNU1HSm1NRGc1TUdVMA; _uetsid=c6ff02703fa311ed859c15a4607c71a4; _uetvid=c6ff2b303fa311ed881da1bdc6d90b0e; has_preloaded=1; qr_is_sr=fast-click; 11_srd=%7B%22features%22%3A%5B%7B%22id%22%3A5%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D; g_state={"i_p":1664433769185,"i_l":1}; _px3=cb4d09c8068c29502a8ad23ec7cc98d73253e998596489172d9e8e65b21195a0:4sbBK8qybTc5o2hKuTJKvTqq9bV7KU4s4youQBw2FQ/VnK/m9tm7VJebwz4J9pVu0sFbJMaMooFqmdNEOj2INw==:1000:WV04La49SMXfu9WAlj9rD9aWqZ1HzmcrBR1xWjgVHlUWOsaAmgAK3VJ67pjRykvce+sUJaQ997UQuZ/8j4rYk4sFegAb3YnjHN0zJCugS6uPf2JYtS40sQrrxZXXeHlkGu8UWFYoTi5SGIplU1ncRpBLtl4ru3/jnkXuF5ZW8vxy5zrGL/HvjZt7GdQS4QH77RfbbFgOHkSMHp7nsSMCbA==; _pxde=201956c7a313ebe8f6238dacc869694a1170fded40d2e9b626b37cac020aa499:eyJ0aW1lc3RhbXAiOjE2NjQ0MjY1ODY1ODYsImZfa2IiOjAsImlwY19pZCI6W119; arp_scroll_position=1500; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbbmD9q%2B5pe3VFUNFW2AZvfBz%2By%2Fmxj4AlqCO0nfOWSCNt37%2Bwxuqro7ry8NQ0g16Tzn99XctWciZAq2UfA4tWeTsVUIZg6wH3UAAurZYOLgQWbN2O8Vc6Iqs5Ug9rnc5cl2BTQ9TxjwmTWxN6J04QapitKIuobqKI1vA9ZOuforA%3D; lastSeen=0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }       
        self.logger.info('test4')
        r= scrapy.http.Request(url, method='GET' , headers = headers, cookies = cookies,)
        r.meta['dont_cache'] = True
        yield r
        

    def parse(self, response):

        # Set the headers here. 
        print(response.body.decode(), file=open("output3.html", "w"))
        if 0:
            s = '#rooms_table > div:nth-child(3) > div > section > div'
            for i in response.css(s)[1:]:
                a=(i.css('span::text')[0].get())
                yield { 'room': a}
        else:
            s2 = '.hprt-roomtype-link'
            # breakpoint()
            for i in response.css(s2)[:]:
                a=(i.css('span::text')[0].get().strip())
                yield { 'room': a}
        # for i in response.css(s)[1:]:
        #     o=i.css('div.ace2775fec::attr(aria-label)').get()
        #     yield { 'max_occupancy': o}
        s= '#hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div >  span.bui-u-sr-only::text'

        #hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div > span.bui-u-sr-only
        for i in response.css(s)[:]:o=i.get().strip();print(f'3{o}2')
        breakpoint()
            # yield { 'max_occupancy': o}