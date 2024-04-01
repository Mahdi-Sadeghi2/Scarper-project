import requests
from bs4 import BeautifulSoup


    
class SearchByCategory:
    def __init__(self,base_url,pages,) -> None:
        self.pages = pages
        self.base_url = base_url

    def search_loop(self):
        total_results = 0
        for i in range(self.pages):
            response = requests.get(self.base_url.format(pages = i))
            data = response.json()
            for d in data['body']:
                print('Category:', d['primary_category']['name'],'\n')
                print('Title:', d['title']['rendered'],'\n')
                cleaned_data = BeautifulSoup(d['excerpt']['rendered'], "html.parser").text
                print('Discription:', cleaned_data)
                date = d['date']
                full_datetime = date
                date, time = full_datetime.split("T")
                print("Published Date:", date,'\n')
                print("Published Time:", time,'\n')
                author_name = d['yoast_head_json']
                print("Author Name:", author_name['author'])
                page_results = len(data['body'])  
                total_results += page_results
                print('*' * 80)
            print("Total results:", total_results)
        


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
