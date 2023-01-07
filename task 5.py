import requests
import bs4


def download_image(root, image_name):
    img_data = requests.get(root + '/' + image_name).content
    with open(f'images/{image_name}', 'wb') as handler:
        handler.write(img_data)


def main(root, url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return
    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    images = soup.find_all('img')
    for img in images:
        download_image(root, img.get('src'))

    links = soup.find_all('a')
    for link in links:
        main(root, url + '/' + link.get('href'))


if __name__ == '__main__':
    main(root='https://beda.pnzgu.ru/anatoly', url='https://beda.pnzgu.ru/anatoly')