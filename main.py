import requests
from basic_methods import BASE_URL

response = requests.get(BASE_URL)

print(response.status_code)
print('*' * 80)
print(response.text)
print('*' * 80)
print(response.headers)
print('*' * 80)