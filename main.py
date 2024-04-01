import requests
from bs4 import BeautifulSoup
from basic_methods import BASE_URL, NUMBER_OF_PAGES, TOTAL_SEARCH_ITEMS, KEYWORD_INPUT


for i in range(TOTAL_SEARCH_ITEMS):
    response = requests.get(BASE_URL.format(keyword= KEYWORD_INPUT, output=i))
    soup = BeautifulSoup(response.text, features="html.parser")
    result = soup.findAll('h4',{'class': 'pb-10'})
    date = soup.findAll('span',{'class': 'pl-15 bl-1-666'})
    author = soup.findAll('span', style='color:#333; font-weight: 700')
    body = soup.findAll('p', style="color: #777")
    link = soup.findAll('a', {'class':'fz-20 lh-22 fw-b'})
    total_result_in_website = [span.text for div in soup.findAll('div', {'class': 'compPagination'}) for span in div.findAll('span')]
        
    for re, de, auth, bo, l, t in zip(result,date,author,body,link, total_result_in_website):
            print('article title:',re.text)
            print('date posted:',de.text)
            print('author:',auth.text)
            print('summary:',bo.text)
            print('link:',l['href'])
            print('total results in website:', t)
            print('total pages number:', NUMBER_OF_PAGES )
            print('total number of the result:', TOTAL_SEARCH_ITEMS)
            total_results = ''.join(filter(str.isdigit, t))
            print('*' * 80)
    if TOTAL_SEARCH_ITEMS > int(total_results):
        print('Your request should be less then the total website results:\n'
                    'total results in website:', total_results,'\nTry again')
        
        break
        


