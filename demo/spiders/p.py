import enum
from bs4 import BeautifulSoup
s = '#rooms_table > div:nth-child(3) > div > section > div'
s= '#hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div'
s = '#hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hp-price-left-align.hprt-table-cell.hprt-table-cell-price.droom_seperator > div > div > div:nth-child(1) > div:nth-child(2) > div > span'

soup = BeautifulSoup(open('output3.html'), 'lxml')
s1 = '#hprt-table tbody tr'
# print first column in the table #hprt-table
rows = []
for tr in soup.select(s1):
    row = []
    for j,td in enumerate( tr.find_all('td')):
        
        p= td.find('span').text.strip()
        p = p.replace(u'\xa0', u' ')
        if p:
            print(j)
            if j == 4:
                continue
            
            row.append(p)
    rows.append(row)
#tabulate the rows
from tabulate import tabulate
# print(tabulate(rows[:1], headers='firstrow', tablefmt='fancy_grid'))
print(rows[0][:])
