
from models import SearchByCategory, SearchByUserInput
from basic_methods import BASE_CATEGORY_URL, BASE_URL
from category_scraper import  user_keyword_input, user_page_number_input, user_pages_input


task = int(
    input('Enter a number:\n1.search by category\n2.search by your input---> '))
if task == 1:
    search_by_category_instance = SearchByCategory(
        BASE_CATEGORY_URL,user_pages_input() )
    search_by_category_instance.search_loop()
elif task == 2:
    search_by_user_input_instance = SearchByUserInput(
        user_pages_input(), BASE_URL, user_keyword_input(), user_page_number_input(),)
    search_by_user_input_instance.search_engine()




# soup = BeautifulSoup(response.text, features="html.parser")
# result = soup.findAll("body",id =2685505)
# for r in result:
#     print(r['date'])
# data = response.json()
# for d in data['body']:
#     print('category:', d['primary_category']['name'],'\n')
#     print('title:', d['title']['rendered'],'\n')
#     cleaned_data = BeautifulSoup(d['excerpt']['rendered'], "html.parser").text
#     print('discription:', cleaned_data)
#     date = d['date']
#     full_datetime = date
#     date, time = full_datetime.split("T")
#     print("Published Date:", date,'\n')
#     print("Published Time:", time,'\n')
#     author_name = d['yoast_head_json']
#     print("Author Name:", author_name['author'])
#     print('*' * 80)

# author_name = data['body'][0]['yoast_head_json']

# date = data['body'][0]['date']
# full_datetime = date
# date, time = full_datetime.split("T")
# print("Published Date:", date)
# print("Published Time:", time)
# print("Author Name:", author_name['author'])

