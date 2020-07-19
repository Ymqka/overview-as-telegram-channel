from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time
import sys

import urllib.request
import shutil
import requests

import config_parser

for i in range(0,20):
    print(i)

sys.exit()


config = config_parser.parse_config()._sections['parser']

# print(config['daily_url'])
# sys.exit()


driver = webdriver.Firefox()

driver.get(config['daily_url'])

soup = BeautifulSoup(driver.page_source, 'lxml')

def parse_post_body_from_html(content_html):
    soup_content = BeautifulSoup(str(content_html), 'lxml')

    post['post_header'] = soup_content.find('h1', class_ ='subheader daily-header').text
    post['post_text']   = soup_content.find('p',  class_ ='body-copy-small overview-description').text
    post['coordinates'] = soup_content.find('p',  class_ ='caption overview-geo').text
    post['posted']      = False

    return post

def parse_link_from_html(link_html):
    soup_link = BeautifulSoup(str(link_html), 'lxml')
    
    url = soup_link.find('a', href=True)['href']

    url_without_params = url.split('?')[0]
    url_with_proper_params = url_without_params + "?" + config['img_params']

    return [url_without_params, url_with_proper_params]

def download_image(url, path_to_image):
    response = requests.get(str(url), stream=True)

    with open(path_to_image, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    return

def get_link_info(url_without_params):
    filename = url_without_params.split('/')[-1]
    path_to_image = config['img_storage'] + filename
    epoch_id = filename.split('-')[0]

    return [path_to_image, epoch_id]


count_posts = 0
# total_posts = []
while True:
    posts = []
    for content_html in soup.findAll('div', class_='daily__OverviewContent-sc-7emf19-4 ebZhgG'):
        post = parse_post_body_from_html(content_html)

        posts.append(post)
        # sys.exit()


    links = []
    for link_html in soup.findAll('div', class_='daily__OverviewImg-sc-7emf19-5 eAIJgU'):
        url_without_params, url_with_proper_params = parse_link_from_html(link_html)

        download_image(url_with_proper_params, path_to_image)

        path_to_image, epoch_id = get_link_info(url_without_params)

        links.append({
            "path_to_image": path_to_image,
            "epoch_id":      epoch_id
        })

        sys.exit()
    if(len(links) == len(posts)):
        for i in range(0, len(links)):
                    
    else:
        logging.error('length of links and length of posts are not equal')

        



    # driver.find_element_by_xpath('//*[@id='w-node-e4d10996b7f3-c6b3f613']/a').click()
    # soup = BeautifulSoup(driver.page_source, 'lxml")
    # time.sleep(5)

