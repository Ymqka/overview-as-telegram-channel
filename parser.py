from bs4 import BeautifulSoup

import requests

import re

import shutil
import os.path


def parse_article(url):
	"""
	Takes url to overview article
	and puts its image into img folder
	and contents into descriptions folder
	"""

    r = requests.get(url)
    if r.status_code != 200:
        return
    soup = BeautifulSoup(r.content, 'lxml')


    #Parsing of title, description and coords
    title = soup.find("title").text
    description = soup.find("p", {"class" : "body-copy-small overview-description"}).text
    coordinates = soup.find("p", {"class" : "caption overview-geo"}).text

    #TODO: Как-то сохранять title, description и coords
    print(title)
    print(description)
    print(coordinates)


    #Parsing of img
    img_link = [i for i in soup.find("picture")][1]["src"]
    img_link = re.findall(r'([^?]+)', img_link)[0]

    response = requests.get(img_link, stream=True)

    name_of_file = url.split("/")[-1] + ".jpg"
    img_filepath = os.path.join("imgs", name_of_file)
    print(img_filepath)

    # сохраняем картинку
    with open(img_filepath, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    del response
