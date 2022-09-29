from bs4 import BeautifulSoup
s = '#rooms_table > div:nth-child(3) > div > section > div'
s= '#hprt-table > tbody > tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block.hprt-table-last-row > td.hprt-table-cell.hprt-table-cell-occupancy.droom_seperator > div > div'
soup = BeautifulSoup(open('output3.html'), 'lxml')
for i in soup.select(s)[:]:
    print(i.text.strip())
    # print(i.find_all('span')[0].text.strip())