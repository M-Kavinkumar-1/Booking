from bs4 import BeautifulSoup
s = '#rooms_table > div:nth-child(3) > div > section > div'
soup = BeautifulSoup(open('output2.html'), 'lxml')
for i in soup.select(s)[1:]:
    print(i.find_all('span')[0].text.strip())