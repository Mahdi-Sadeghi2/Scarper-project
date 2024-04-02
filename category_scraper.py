from basic_methods import DEFAULT_KEYWORD_INPUT, DEFAULT_NUMBER_OF_PAGES
import requests
from bs4 import BeautifulSoup
from datasaver.models import ArticlCategory, ArticleBasedSearch
from django.utils.dateparse import parse_date, parse_time


class SearchByCategory:
    def __init__(self, base_url, pages,) -> None:
        self.pages = pages
        self.base_url = base_url

    def search_loop(self):
        total_results = 0
        for i in range(1, self.pages+1):
            response = requests.get(self.base_url.format(pages=i))
            data = response.json()
            for d in data['body']:
                articel = ArticlCategory.objects.create(

                    category=d['primary_category']['name'],
                    title=d['title']['rendered'],
                    discription=BeautifulSoup(
                        d['excerpt']['rendered'], "html.parser").text,
                    Published_Date=parse_date(d['date']),
                    published_time=parse_time(d['date']),
                    author=d['yoast_head_json']['author'],
                    image_url=d['yoast_head_json']['og_image'][0]['url'],
                    articl_link=d['link']



                )
                articel.save()
                page_results = len(data['body'])
                total_results += int(page_results / 10)
                print('*' * 80)
            print("Total results:", total_results)


class SearchByUserInput:
    def __init__(self, pages, url, keyword, total_search) -> None:
        self.pages = pages
        self.url = url
        self.keyword = keyword
        self.total_search = total_search

    def search_engine(self):
        for i in range(1, int(self.total_search * 10)+1):
            response = requests.get(self.url.format(
                keyword=self.keyword, output=i))
            soup = BeautifulSoup(response.text, features="html.parser")
            result = soup.findAll('h4', {'class': 'pb-10'})
            date = soup.findAll('span', {'class': 'pl-15 bl-1-666'})
            author = soup.findAll('span', style='color:#333; font-weight: 700')
            body = soup.findAll('p', style="color: #777")
            link = soup.findAll('a', {'class': 'fz-20 lh-22 fw-b'})
            total_result_in_website = [span.text for div in soup.findAll(
                'div', {'class': 'compPagination'}) for span in div.findAll('span')]

            for re, de, auth, bo, l, t in zip(result, date, author, body, link, total_result_in_website):
                article = ArticleBasedSearch.objects.create(
                    title=re.text,
                    date_posted=de.text,
                    authors=auth.text,
                    summary=bo.text,
                    link=l['href'],
                    keywords=self.keyword,
                    websit_total_results=t
                )
                article.save()
                print('Saved articl', article)
                # print('total results in website:', t)
                print('total pages number:', self.pages)
                print('total number of the result:', self.total_search)
                total_results = ''.join(filter(str.isdigit, t))
                print('*' * 80)
            if self.total_search > int(total_results):
                print('Your request should be less then the total website results:\n'
                      'total results in website:', total_results, '\nTry again')
                break


page = list()


def user_pages_input(pages=None):
    pages = int(input('Enter a number for pages:---> ')
                or DEFAULT_NUMBER_OF_PAGES)
    page.append(pages)
    pages = int(''.join(map(str, page)))
    return pages


def user_page_number_input(search_page=None):
    pages = int(''.join(map(str, page)))
    search_page = pages * 10
    return search_page


def user_keyword_input(keyword=None):
    keyword = input(
        'Enter your keyword for search:---> ') or DEFAULT_KEYWORD_INPUT
    return (keyword)
