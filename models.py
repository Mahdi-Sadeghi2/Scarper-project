import requests
from bs4 import BeautifulSoup


    
class SearchByCategory:
    def __init__(self,base_url,category,) -> None:
        self.category = category
        self.base_url = base_url

    def search_loop(self):
        response = requests.get(self.base_url.format(categories = self.category))
        soup = BeautifulSoup(response.text, features="html.parser")
        result = soup.findAll('a',{'class': 'post-block__title__link'})
        summary = soup.findAll('div',{'class': 'post-block__content'})
        category = self.category
        if self.category == 'artificial-intelligence':
            category = 'AI'
        elif self.category == 'cryptocurrency':
            category = 'Crypto'
        elif self.category == 'Government-policy':
            category = 'Government & Policy'
        elif self.category == 'Biotech-health':
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
        


class SearchByUserInput:
    def __init__(self,pages,url,keyword,total_search) -> None:
        self.pages = pages
        self.url = url
        self.keyword = keyword
        self.total_search = total_search
    
    def search_engine(self):
        for i in range(self.total_search):
            response = requests.get(self.url.format(keyword= self.keyword, output=i))
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
                    print('total pages number:', self.pages )
                    print('total number of the result:', self.total_search)
                    total_results = ''.join(filter(str.isdigit, t))
                    print('*' * 80)
            if self.total_search > int(total_results):
                print('Your request should be less then the total website results:\n'
                            'total results in website:', total_results,'\nTry again')
                break
