import requests
from bs4 import BeautifulSoup

URL = 'https://beda.pnzgu.ru/anatoly/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


images = soup.find_all('img')


for image in images:
    image_url = image['src']
    if not image_url.startswith('https://'):
        image_url = URL + image_url
    image_data = requests.get(image_url).content
    image_name = image_url.split('/')[-1]
    with open(image_name, 'wb') as f:
        f.write(image_data)
