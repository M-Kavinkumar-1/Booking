# -*- coding: utf-8 -*-
from tracemalloc import start
import scrapy
import random

#import logging
cookies = {
    'px_init': '0',
    'cors_js': '1',
    'bkng_frontend_sese_exp': '1',
    'OptanonConsent': 'implicitConsentCountry=nonGDPR&implicitConsentDate=1664420813100',
    '_pxvid': 'c2207f96-3fa3-11ed-99c6-65435468596c',
    '_px_f394gi7Fvmc43dfg_user_id': 'YzYzNDc4NjEtM2ZhMy0xMWVkLTlhY2YtY2JiMzkwYzBlOWI1',
    '_gcl_au': '1.1.733817114.1664420816',
    '_scid': '14cf6a01-9758-4c96-9214-09f01fb9b09a',
    '_sctr': '1|1664389800000',
    '_pin_unauth': 'dWlkPVpUTTFPR05oTUdNdE56SmpPQzAwTTJNNUxXRmxObVl0TkRrNU1HSm1NRGc1TUdVMA',
    'px_init': '0',
    '_gid': 'GA1.2.914755086.1664713993',
    'BJS': '-',
    'pxcts': '624f1e52-424e-11ed-9fb5-4c4352726171',
    'bkng_prue': '1',
    'has_preloaded': '1',
    'g_state': '{"i_p":1665318873037,"i_l":3}',
    'bkng_sso_ses': 'eyJib29raW5nX2dsb2JhbCI6W3siaCI6IjE4R0NOc1h4SHVQUGFJWGF1T2VWN2ZoU29hZ25EMHdOdmJHQjNhVnJRWk0ifV19',
    'bkng_sso_session': 'eyJib29raW5nX2dsb2JhbCI6W3sibG9naW5faGludCI6IjE4R0NOc1h4SHVQUGFJWGF1T2VWN2ZoU29hZ25EMHdOdmJHQjNhVnJRWk0ifV19',
    '_pxhd': 'GAg2R1FcaRuxb2EZEGD5RoTSm2UX6hWYbySBW-a65KbRJgU8pjxPOPOIA5ODU7b5sSibVtBWT7S5T2FlGO9Ccw%3D%3D%3AFTU-E4-ZBP7kRHbBMehLszbLUT5oVS9pWnDF6I%2F3D1pjhV5EPpazW4T7lbcRo1bDpWRmeEPsPOXzIMlcPur-yq2JcDUvRynNkh4r7TQDZpQ%3D',
    '_gat': '1',
    '_pxff_rf': '1',
    '_pxff_ddtc': '1',
    '_uetsid': '64946850424e11ed91de65ff6bd3d466',
    '_uetvid': 'c6ff2b303fa311ed881da1bdc6d90b0e',
    '_ga_FPD6YLJCJ7': 'GS1.1.1664784684.10.1.1664786103.0.0.0',
    '_ga': 'GA1.1.331326721.1664420813',
    '_px3': '47d2a806be4393f74492a68144b382afe3943a1723aa62fa52de7713e36ee6dc:QK8WWKT+LMCMeweneRk5Xh3GTFmDdl2rCocwNG6HyLt3Fj+eCueh0/EU5ozUmOPjWQKv55dTNBkHeYRAzIj6Iw==:1000:xlYCx5mbuSwry3l/KlmR0UPyXlna1FR3yyZ3t7HRCuvy2Ru2jCg/2gZubmbwvFy+xqy20mLRckoyFC+acXSI8x/Og6Yy5fw4g6a+a3H4Fe9sJ6RlLEKUUqVMaDHcp3tS2gAC4xr/OQMr6kzDAXj5xibr/oEn1SO3SaKpwWRlmi7n44rm4n7mLm0zQ6wl+uI4DmD0om17sCsoLh1fUEw0vQ==',
    '_pxde': 'ab1ea05c8f1348c36894b233d941dea6b7b69b31e98b49df0698264d86179109:eyJ0aW1lc3RhbXAiOjE2NjQ3ODYxMDU0MzcsImZfa2IiOjAsImlwY19pZCI6W119',
    '_derived_epik': 'dj0yJnU9NkpvUWF3T2FuYnVFRWVvRnVNZnZrdGtqYXVNMWtYdEsmbj13c0g2VHotVklLSHFRTVRKcTNDQ3Z3Jm09NCZ0PUFBQUFBR002bnJvJnJtPTQmcnQ9QUFBQUFHTTZucm8',
    'cto_bundle': 'xSm1Ql9VZCUyQjNWbmNvbVNRT2RpZk5CbzRyME9ncmdpRmJ1VllqNXJ2MFh6YmpMa0dwMUhxdHNyajFKOCUyQmE1VU1aaFQ1SnFDYkxiTEJtYlJpQWVEakZmTlYyV2ZtNTJWUVYlMkZhSWxYZUZpRlU0UiUyQm5NWXF5Tll2bE85N3hEWEslMkZDRVZveiUyRnZqaDBNMjVvV1ljRXFXTHklMkJsZXE4dyUzRCUzRA',
    'arp_scroll_position': '1268',
    'lastSeen': '0',
    'bkng': '11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbmlZgMctCRAatp%2Bo3zB97IYDb6K0RhvSnwoahUsDS8L%2Bl%2FK8uVj95FOYppGRSF5zci5ahi6Be5pYYATTeNsZjiRgjEk5VfmABInBgZ74kwAECoTRIPKXFxh2yvbVlF5Jwx53WbB1XVFZiz%2BGWXEarG7rquFMlrdjMveP4CgnHRnSqlIi%2B9Bwqv%2BGw9YAfRyqmr5x2MO6jaYhQkE%2FLdbQ%2F0NHRoYVTohUA',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'px_init=0; cors_js=1; bkng_frontend_sese_exp=1; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1664420813100; _pxvid=c2207f96-3fa3-11ed-99c6-65435468596c; _px_f394gi7Fvmc43dfg_user_id=YzYzNDc4NjEtM2ZhMy0xMWVkLTlhY2YtY2JiMzkwYzBlOWI1; _gcl_au=1.1.733817114.1664420816; _scid=14cf6a01-9758-4c96-9214-09f01fb9b09a; _sctr=1|1664389800000; _pin_unauth=dWlkPVpUTTFPR05oTUdNdE56SmpPQzAwTTJNNUxXRmxObVl0TkRrNU1HSm1NRGc1TUdVMA; px_init=0; _gid=GA1.2.914755086.1664713993; BJS=-; pxcts=624f1e52-424e-11ed-9fb5-4c4352726171; bkng_prue=1; has_preloaded=1; g_state={"i_p":1665318873037,"i_l":3}; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siaCI6IjE4R0NOc1h4SHVQUGFJWGF1T2VWN2ZoU29hZ25EMHdOdmJHQjNhVnJRWk0ifV19; bkng_sso_session=eyJib29raW5nX2dsb2JhbCI6W3sibG9naW5faGludCI6IjE4R0NOc1h4SHVQUGFJWGF1T2VWN2ZoU29hZ25EMHdOdmJHQjNhVnJRWk0ifV19; _pxhd=GAg2R1FcaRuxb2EZEGD5RoTSm2UX6hWYbySBW-a65KbRJgU8pjxPOPOIA5ODU7b5sSibVtBWT7S5T2FlGO9Ccw%3D%3D%3AFTU-E4-ZBP7kRHbBMehLszbLUT5oVS9pWnDF6I%2F3D1pjhV5EPpazW4T7lbcRo1bDpWRmeEPsPOXzIMlcPur-yq2JcDUvRynNkh4r7TQDZpQ%3D; _gat=1; _pxff_rf=1; _pxff_ddtc=1; _uetsid=64946850424e11ed91de65ff6bd3d466; _uetvid=c6ff2b303fa311ed881da1bdc6d90b0e; _ga_FPD6YLJCJ7=GS1.1.1664784684.10.1.1664786103.0.0.0; _ga=GA1.1.331326721.1664420813; _px3=47d2a806be4393f74492a68144b382afe3943a1723aa62fa52de7713e36ee6dc:QK8WWKT+LMCMeweneRk5Xh3GTFmDdl2rCocwNG6HyLt3Fj+eCueh0/EU5ozUmOPjWQKv55dTNBkHeYRAzIj6Iw==:1000:xlYCx5mbuSwry3l/KlmR0UPyXlna1FR3yyZ3t7HRCuvy2Ru2jCg/2gZubmbwvFy+xqy20mLRckoyFC+acXSI8x/Og6Yy5fw4g6a+a3H4Fe9sJ6RlLEKUUqVMaDHcp3tS2gAC4xr/OQMr6kzDAXj5xibr/oEn1SO3SaKpwWRlmi7n44rm4n7mLm0zQ6wl+uI4DmD0om17sCsoLh1fUEw0vQ==; _pxde=ab1ea05c8f1348c36894b233d941dea6b7b69b31e98b49df0698264d86179109:eyJ0aW1lc3RhbXAiOjE2NjQ3ODYxMDU0MzcsImZfa2IiOjAsImlwY19pZCI6W119; _derived_epik=dj0yJnU9NkpvUWF3T2FuYnVFRWVvRnVNZnZrdGtqYXVNMWtYdEsmbj13c0g2VHotVklLSHFRTVRKcTNDQ3Z3Jm09NCZ0PUFBQUFBR002bnJvJnJtPTQmcnQ9QUFBQUFHTTZucm8; cto_bundle=xSm1Ql9VZCUyQjNWbmNvbVNRT2RpZk5CbzRyME9ncmdpRmJ1VllqNXJ2MFh6YmpMa0dwMUhxdHNyajFKOCUyQmE1VU1aaFQ1SnFDYkxiTEJtYlJpQWVEakZmTlYyV2ZtNTJWUVYlMkZhSWxYZUZpRlU0UiUyQm5NWXF5Tll2bE85N3hEWEslMkZDRVZveiUyRnZqaDBNMjVvV1ljRXFXTHklMkJsZXE4dyUzRCUzRA; arp_scroll_position=1268; lastSeen=0; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbmlZgMctCRAatp%2Bo3zB97IYDb6K0RhvSnwoahUsDS8L%2Bl%2FK8uVj95FOYppGRSF5zci5ahi6Be5pYYATTeNsZjiRgjEk5VfmABInBgZ74kwAECoTRIPKXFxh2yvbVlF5Jwx53WbB1XVFZiz%2BGWXEarG7rquFMlrdjMveP4CgnHRnSqlIi%2B9Bwqv%2BGw9YAfRyqmr5x2MO6jaYhQkE%2FLdbQ%2F0NHRoYVTohUA',
    'Referer': 'https://www.booking.com/hotel/ca/kimbrook-lodge.en-gb.html?aid=304142&label=gen173nr-1FCAsoJ0IOa2ltYnJvb2stbG9kZ2VICVgEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AqGu1ZkGwAIB0gIkMTQyNTJmMTAtYjBhNy00YTU1LWFlNmQtNDk1YjYyMjgxNDZl2AIF4AIB&sid=b0aeead7ef43aa19121bec2107fe17cc&checkin_month=10&checkin_monthday=4&checkin_year=2022&checkout_month=10&checkout_monthday=5&checkout_year=2022&dist=0&do_availability_check=1&group_adults=2&group_children=0&highlighted_blocks=415757601_297096113_0_1_0&hp_avform=1&hp_group_set=0&hp_sbox=1&no_rooms=1&origin=hp&sb_price_type=total&src=hotel&stay_on_hp=1&type=total&',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'aid': '304142',
    'label': 'gen173nr-1FCAsoJ0IOa2ltYnJvb2stbG9kZ2VICVgEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AqGu1ZkGwAIB0gIkMTQyNTJmMTAtYjBhNy00YTU1LWFlNmQtNDk1YjYyMjgxNDZl2AIF4AIB',
    'sid': 'b0aeead7ef43aa19121bec2107fe17cc',
    'checkin_month': '10',
    'checkin_monthday': '4',
    'checkin_year': '2022',
    'checkout_month': '10',
    'checkout_monthday': '5',
    'checkout_year': '2022',
    'dist': '0',
    'do_availability_check': '1',
    'group_adults': '2',
    'group_children': '0',
    'highlighted_blocks': '415757601_297096113_0_1_0',
    'hp_avform': '1',
    'hp_group_set': '0',
    'hp_sbox': '1',
    'no_rooms': '1',
    'origin': 'hp',
    'sb_price_type': 'total',
    'src': 'hotel',
    'stay_on_hp': '1',
    'type': 'total',
}
class AaidSpider(scrapy.Spider):
    name = 'a'
    # start_urls = ['http://x.com/']
   
    
    def parse(self, response):
        self.logger.info('test5')
        print(response, response.body)
        pass
    def start_requests(self):

        url = "https://www.booking.com/hotel/ca/kimbrook-lodge.en-gb.html"+ "?dummy=" + str(random.random())
        

          
        self.logger.info('test4')
        r= scrapy.http.FormRequest(url, method='GET' , headers = headers, cookies = cookies,formdata = params)
        r.meta['dont_cache'] = True
        yield r
        

    def parse(self, response):

        # Set the headers here. 
        print(response.body.decode(), file=open("output3.html", "w"))
        # if 0:
        #     s = '#rooms_table > div:nth-child(3) > div > section > div'
        #     for i in response.css(s)[1:]:
        #         a=(i.css('span::text')[0].get())
        #         yield { 'room': a}
        # else:
        #     s2 = '.hprt-roomtype-link'
        #     # breakpoint()
        #     for i in response.css(s2)[:]:
        #         a=(i.css('span::text')[0].get().strip())
        #         yield { 'room': a}
        # for i in response.css(s)[1:]:
        #     o=i.css('div.ace2775fec::attr(aria-label)').get()
        #     yield { 'max_occupancy': o}
        s= '#hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div >  span.bui-u-sr-only::text'

        #hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div > span.bui-u-sr-only
        # for i in response.css(s)[:]:o=i.get().strip();print(f'3{o}2')
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(open('booking.html'), 'lxml')
        s1 = '#hprt-table tbody tr'
        # print first column in the table #hprt-table
        rows = []
        for tr in soup.select(s1):
            row = []
            for j,td in enumerate( tr.find_all('td')):
                if j == 0:
                    #title
                    c = "hprt-roomtype-block hprt-roomtype-name hp_rt_room_name_icon__container"
                    title = td.find('div', class_=c).text.strip()
                    #beds count
                    c = 'hprt-roomtype-bed'
                    bed_count = td.find('div', class_=c).text.strip()
                    # print(bed_count)
                    #room_info
                    c = 'bui-spacer--medium'
                    room_info = td.find('div', class_=c)
                    room_info = [i.text.strip() for i in room_info.find_all('div')]
                    # print(room_info)
                    # exit()
                    c = 'hprt-facilities-others'
                    room_amenity = td.find('ul', class_=c)
                    room_amenity = [i.text.strip() for i in room_amenity.find_all('li')]
                    # print(room_am)
                    # exit()
                elif j==1:
                    max_occupancy = td.text.strip().split(': ')[-1]
                elif j==2:
                    # print(td.text.strip())
                    # exit()
                    c = 'prco-valign-middle-helper'
                    price = td.find('span', class_=c).text.strip().replace('\xa0', '')
                    # print(price)
                    # exit()
                    c = 'prd-taxes-and-fees-under-price'
                    taxes = td.find('div', class_=c).text.strip().replace('\xa0', '')
                    # print(taxes)
                elif j==3:
                    c= 'bui-list__description'
                    food = td.find('div', class_=c).text.strip()
                    # print(food)
                    # exit()
                    c = 'e2e-cancellation'
                    rate_plan_info = td.find('li', class_=c).text.strip().replace('\n', ' ')

            # exit()
            row.append([title, bed_count, room_info, room_amenity, price, taxes, food, rate_plan_info])
            #convert to json  
            j = {
                'title': title,
                'bed_count': bed_count,
                'room_info': room_info,
                'room_amenity': room_amenity,
                'max_occupancy' : max_occupancy,
                'price': price,
                'taxes': taxes,
                'food': food,
                'rate_plan_info': rate_plan_info
            }
            yield (j)
            # rows.append(row)
        # #tabulate the rows
        # from tabulate import tabulate
        # # print(tabulate(rows[:1], headers='firstrow', tablefmt='fancy_grid'))
        # import re
        # a= re.sub(r'\n+','\n', rows[0][0])
        # print(a.split('\n'))
        # print(a)

        # breakpoint()
        
            # yield { 'max_occupancy': o}
