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

            pass
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
    from pprint import pprint
    pprint(j)
    rows.append(row)
#tabulate the rows
from tabulate import tabulate
# print(tabulate(rows[:1], headers='firstrow', tablefmt='fancy_grid'))
import re
# a= re.sub(r'\n+','\n', rows[0][0])
# print(a.split('\n'))
# print(a)
