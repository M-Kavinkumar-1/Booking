# -*- coding: utf-8 -*-
import datetime
import json
import traceback

import db
import htmlmin
import scrapy
from config import headers
from pymsgbox import alert


class AaidSpider(scrapy.Spider):
    name = 'a'
    db = db.DB(initiate=1)
    # start_urls = ['http://x.com/']

    def start_requests(self):
        # ii = [(1001, 1, 2, 'https://www.booking.com/hotel/in/avenue-11.html?label=gen173nr-1DCAsobEIJYXZlbnVlLTDNEpUTHQoQUJMHLrErGJyHg89uy71MyuHB-AEDiAIBqAIDuAKP1LqaBsACAdICJGI5ODJlZjI3LWE4MjktNDNlZi05YTY4LWY4YWM4ODhhMDBhNNgCBOACAQ&sid=617cdc3dc8a1562cc09c1c872b2a08ec&checkin=2022-10-20&checkout=2022-10-21&dist=0&group_adults=1&keep_landing=1&sb_price_type=total&type=total&',
            #    0, 'USD', datetime.date(2023, 5, 3), datetime.date(2023, 5, 5), datetime.date(2022, 10, 22), 1)]

        # for k,i in enumerate(ii,1):
        for k, i in enumerate(self.db.read()[:], 1):
            print('Scraping', k,)
            # ['id', 'hotelcode', 'websitecode', 'url', 'status', 'curr', 'checkindate', 'checkoutdate', 'dtcollected', 'guests']
            url = i[3]
            url = url.replace('{chkin}', i[6].strftime('%Y-%m-%d'))
            url = url.replace('{chkout}', i[7].strftime('%Y-%m-%d'))
            url = url.replace('{guest}', str(i[9]))
            url = url.replace('{currency}', i[5])
            yield scrapy.http.FormRequest(url, method='GET', headers=headers,  callback=self.parse, meta={'input': i, 'url': url})

    def parse(self, response):
        html = response.body.decode()
        # Set the headers here.
        # print(response.body.decode(), file=open("booking.html", "w"))
        s = '#hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div >  span.bui-u-sr-only::text'
        id, hotelcode, websitecode, url, status, curr, checkindate, checkoutdate, dtcollected, guests = response.meta.get(
            'input')
        url = response.meta.get('url')
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'lxml')
        s1 = '#hprt-table tbody'
        rows = []
        rowspan = None
        first_row = -1
        s1 = '#hprt-table tbody'
        rows = []
        table = soup.select(s1)
        trs = soup.select('#hprt-table tbody tr')
        rooms = []
        rowspan = None
        first_row = -1
        try:
            for tr_k, tr in enumerate(trs):
                row = []
                for j, td in enumerate(tr.find_all('td')):
                    if rowspan and tr_k != first_row:
                        j = j+1
                    if j == 0:
                        # title
                        c = "hprt-roomtype-block hprt-roomtype-name hp_rt_room_name_icon__container"
                        try:
                            title = td.find(class_=c).text.strip()
                            # get attribute of rowspan
                            rowspan = int(td.get('rowspan'))
                            if rowspan:
                                first_row = tr_k
                        except Exception as e:
                            traceback.print_exc()
                            print(rowspan, j, tr_k)
                            exit()
                        # beds count
                        c = 'hprt-roomtype-bed'
                        bed_count = td.find('div', class_=c).text.strip()
                        # print(bed_count)
                        # room_info
                        c = 'bui-spacer--medium'
                        room_info = td.find('div', class_=c)
                        room_info = [i.text.strip()
                                     for i in room_info.find_all('div')]
                        # print(room_info)
                        # exit()
                        c = 'hprt-facilities-others'
                        room_amenity = td.find('ul', class_=c)
                        room_amenity = [i.text.strip()
                                        for i in room_amenity.find_all('li')]
                        # print(room_am)
                        # exit()
                    # if rowspan and j!=0:
                    #      j-=1
                    elif j == 1:
                        max_occupancy = td.text.strip().split(': ')[-1]
                    elif j == 2:
                        # print(td.text.strip())
                        # exit()
                        c = 'prco-valign-middle-helper'
                        # print(td)
                        price = td.find(
                            'span', class_=c).text.strip().replace('\xa0', '')
                        try:
                            c = f'#hprt-table > tbody > tr:nth-child({tr_k+1}) > td.hp-price-left-align.hprt-table-cell.hprt-table-cell-price > div > div.prco-wrapper.bui-price-display.prco-sr-default-assembly-wrapper > div:nth-child(1) > div:nth-child(1) > div'
                            netrate = soup.select(
                                c)[0].text.strip().replace('\xa0', '')
                            # print(netprice,'n')
                        except:
                            netrate = None
                        # print(price)
                        # exit()
                        c = 'prd-taxes-and-fees-under-price'
                        taxes = td.find(
                            'div', class_=c).text.strip().replace('\xa0', '')
                        # print(taxes)
                    elif j == 3:
                        c = 'bui-list__description'
                        food = td.find('div', class_=c).text.strip()
                        # print(food)
                        # exit()
                        c = 'e2e-cancellation'
                        rate_plan_info = td.find(
                            'li', class_=c).text.strip().replace('\n', ' ')
                if rowspan:
                    rowspan -= 1
                # exit()

                row = [title, bed_count, room_info, room_amenity,
                       price, taxes, food, rate_plan_info]
                rows.append(row)
                # print(len(table))
                # print(json)

                # convert to json
                j = {
                    "hotelcode": hotelcode,
                    "websitecode": websitecode,
                    "dtcollected": dtcollected.strftime('%Y-%m-%d'),
                    # "ratedate":  checkindate.strftime('%Y-%m-%d'),
                    # "los": 1,
                    # "guests": 1,
                    "roomtype": title,
                    "room_description": room_info,
                    "onsiterate": price,
                    "maxoccupancy": max_occupancy,
                    "roomamenities": room_amenity,
                    "netrate": netrate,
                    "currency": curr,
                    "ratedescription": rate_plan_info,
                    # "ratetype": "null",
                    "sourceurl": url,
                    # "ispromo": "N",
                    # "closed": "Y",
                    "checkin": checkindate.strftime('%Y-%m-%d'),
                    "checkout": checkoutdate.strftime('%Y-%m-%d'),
                    # "discount": 0,
                    # "promoname": "",
                    # "searchkeyword": null,
                    # "roomtypecode": 2,
                    # "conditionscode": null,
                    # "mealplancode": null,
                    # "taxstatus": null,
                    # "taxtype": taxes,
                    "taxamount": taxes,
                    # "pos": 0,
                    # "israteperstay": "",
                    # "status_code": 202,
                    "meal_plan_info": food,
                }
                rooms.append(j)
        except Exception as e:
            rooms = {"parse_error": str(e), "url": url}
        if not table:
            rooms = {'error': 'no table', 'url': url}
        jsondata = json.dumps(rooms)
        if table:
            minified_html_data = htmlmin.minify(
                str(table[0]), remove_empty_space=True)
        else:
            minified_html_data = 'No Data'
        self.db.store(hotelcode, websitecode, jsondata,
                      minified_html_data, checkindate, id)
        self.db.update(id=id, status=1 if table else 2)


if __name__ == '__main__':
    from scrapy.cmdline import execute

    # log level error
    execute('scrapy crawl a -O a.json -L ERROR '.split())
    # execute('scrapy crawl a -O a.json '.split())
    alert("Done")
