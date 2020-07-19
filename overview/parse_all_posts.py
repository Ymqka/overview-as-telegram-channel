from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time
import sys
import logging

import parser
import utils

args   = utils.parse_arguments()
config = utils.parse_config(args.config)

logging.basicConfig(
    filename=config['utils']['log_filepath'],
    level=logging.INFO, 
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

overview_db = utils.OverView_db(config['overview'])

parser_config = config['parser']

driver = webdriver.Firefox()
driver.get(parser_config['daily_url'])

soup = BeautifulSoup(driver.page_source, 'lxml')

total_posts = []
while True:
    posts = []
    for content_html in soup.findAll('div', class_='daily__OverviewContent-sc-7emf19-4 ebZhgG'):
        post = parser.parse_post_body_from_html(content_html)

        posts.append(post)


    links = []
    for link_html in soup.findAll('div', class_='daily__OverviewImg-sc-7emf19-5 eAIJgU'):
        url_without_params, url_with_proper_params = parser.parse_link_from_html(link_html, parser_config['img_params'])

        path_to_image, epoch_id = parser.get_link_info(url_without_params, parser_config['img_storage'])

        parser.download_image(url_with_proper_params, path_to_image)

        links.append({
            "path_to_image": path_to_image,
            "epoch_id":      int(epoch_id)
        })
        logging.info('going to sleep 3 secs')
        time.sleep(3)


    if(len(links) == len(posts)):
        for i in range(0, len(links)):
            post = {**(posts[i]), **(links[i])}
            total_posts.append(post)
            logging.info("succesfully processed " + len(posts) + ' posts')
    else:
        logging.error('length of links and length of posts are not equal, url: ' + driver.current_url)

    driver.find_element_by_xpath("//*[@id='w-node-e4d10996b7f3-c6b3f613']/a").click()
    soup = BeautifulSoup(driver.page_source, 'lxml')

    logging.info('going to sleep 10 secs')
    time.sleep(10)

logging.info('succesfully processed ' + len(total_posts) + ' posts')
overview_db.add_posts(total_posts)
