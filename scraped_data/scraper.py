from bs4 import BeautifulSoup as bs
page= open('page.html', 'r')
soup = bs(page, 'html.parser')
faculty = soup.find_all('div',class_='faculty')
data = []
for i in faculty:
    data.append(i.text.strip().replace('\n', ','))
dataforskl= open('dataforselect.txt','w')
for i in data:
    print(i)
    dataforskl.write(i+'\n')
dataforskl.close()
