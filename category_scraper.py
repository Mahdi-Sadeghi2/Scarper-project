import requests
from bs4 import BeautifulSoup

from basic_methods import  BASE_CATEGORY_URL, CATEGORIES

response = requests.get(BASE_CATEGORY_URL.format(categories = CATEGORIES))
soup = BeautifulSoup(response.text, features="html.parser")
result = soup.findAll('a',{'class': 'post-block__title__link'})
summary = soup.findAll('div',{'class': 'post-block__content'})
category = CATEGORIES
if CATEGORIES == 'artificial-intelligence':
    category = 'AI'
elif CATEGORIES == 'cryptocurrency':
    category = 'Crypto'
elif CATEGORIES == 'Government-policy':
    category = 'Government & Policy'
elif CATEGORIES == 'Biotech-health':
    category = 'Biotech & Health'
else:
    category
author = soup.findAll('span', {'class':'river-byline__authors'})
link = soup.findAll('a', {'class':'post-block__title__link'})
image = soup.findAll('img')
for re, s, a, l, i, in zip(result, summary,author,link,image):
    print('title:',re.text.strip(),'\n')
    print('image:',i['srcset'].split()[4],'\n')
    print('summary:',s.text.strip()+'.','\n')
    print('author:',a.text.strip(),'\n')
    print('article link:',l['href'])
    print('category:',category)
    print('*' * 80)
print('Length:', len(result))


