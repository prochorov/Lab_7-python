import requests

URL = 'https://beda.pnzgu.ru/anatoly/'

response = requests.get(URL)

print(response.text)
