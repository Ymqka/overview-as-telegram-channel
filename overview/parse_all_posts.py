from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

import time
import sys
import logging

import parser
import utils

args   = utils.parse_arguments()
config = utils.parse_config(args.config)

logging.basicConfig(
    filename = 'overview.log',
    level=logging.INFO, 
    format= '[%(asctime)s] %(levelname)s - %(message)s {%(pathname)s:%(lineno)d}',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

overview_db = utils.OverView_db(config['overview'])

parser_config = config['parser']

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(parser_config['daily_url'])

soup = BeautifulSoup(driver.page_source, 'lxml')

posts_content_counter = links_counter = total_posts_counter = 0

while True:
    posts = []
    for content_html in soup.findAll('div', class_='daily__OverviewContent-sc-7emf19-4 ebZhgG'):
        post = parser.parse_post_body_from_html(content_html)

        posts_content_counter += 1

        posts.append(post)

    logging.info('processed ' + str(posts_content_counter) + ' posts_content')

    links = []
    for link_html in soup.findAll('div', class_='daily__OverviewImg-sc-7emf19-5 eAIJgU'):
        url_without_params, url_with_proper_params = parser.parse_link_from_html(link_html, parser_config['img_params'])

        path_to_image, epoch_id = parser.get_link_info(url_without_params, parser_config['img_storage'])

        logging.info('going to dowload image from ' + str(url_with_proper_params) + ' url to ' + path_to_image)

        parser.download_image(url_with_proper_params, path_to_image)

        links.append({
            "path_to_image": path_to_image,
            "epoch_id":      int(epoch_id)
        })

        links_counter += 1

        logging.info('processed ' + str(links_counter) + ' links')
        logging.info('going to sleep 3 secs')
        time.sleep(3)

    posts_to_db = []   
    if(len(links) == len(posts)):
        for i in range(0, len(links)):
            post = {**(posts[i]), **(links[i])}
            posts_to_db.append(post)
    else:
        logging.error('length of links and length of posts are not equal, url: ' + driver.current_url)
        bot_token = os.environ['bot_token']
        devs_id = os.environ['devs_id'].split(',')
        utils.alert_developers(bot_token, devs_id)

    driver.find_element_by_xpath("//*[@id='w-node-e4d10996b7f3-c6b3f613']/a").click()
    soup = BeautifulSoup(driver.page_source, 'lxml')

    total_posts_counter += len(posts_to_db)
    overview_db.add_posts(posts_to_db)

    logging.info('going to sleep 10 secs')
    time.sleep(10)

logging.info("successfully processed " + total_posts_counter + " posts")