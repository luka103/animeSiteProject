from random import *
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

h = {'Accept-Language': 'en-US'}
file = open('anime.csv', 'w', newline='\n', encoding="utf-8")
f_obj = csv.writer(file)
f_obj.writerow(['Title', 'Info', 'Rating', 'IMG_URL'])

page = 0
while page < 250:
    url = 'https://myanimelist.net/topanime.php?limit=' + str(page)
    r = requests.get(url, headers=h)
    print(r.headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_='pb12')
    all_anime = sub_soup.findAll('tr', class_='ranking-list')
    for each in all_anime:
        img_url = each.img.get('data-src')
        title = each.h3.a.text
        info = each.find('div', class_='information di-ib mt4').text.strip()
        rating = each.find('div', class_='js-top-ranking-score-col di-ib al').text
        print(title)
        f_obj.writerow([title, info, rating, img_url])
    page += 50
    sleep(randint(15, 20))
