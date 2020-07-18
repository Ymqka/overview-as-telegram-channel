from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import re

import urllib.request
import shutil
import requests


# sys.exit()

from bs4 import BeautifulSoup

driver = webdriver.Firefox()

driver.get('https://www.over-view.com/daily/')

soup = BeautifulSoup(driver.page_source, 'lxml')



# <a class='nav-menu-link' href='/daily/2'>Next</a>
    # for text in soup.findAll('h1', class_='subheader daily-header'):
    #     print(text)

# <div class='daily__OverviewContent-sc-7emf19-4 ebZhgG'><h1 id='w-node-0e4a4f7ac915-5940d611' class='subheader daily-header'>Pingyuan Reservoir</h1><p class='body-copy-small overview-description'>Clear blue water fills the Pingyuan Reservoir, located just outside of Zhaodong City in northeastern China. Water stored here serves the more than 100,000 inhabitants of Zhaodong and surrounding farms of Heilongjiang Province, which grow soybeans, maize, wheat, potatoes, beets and flax. For a sense of scale, the Pingyuan Reservoir covers about 1.32 square miles (3.4 square kilometers) — roughly the same area as Central Park in Manhattan.</p><p class='caption overview-geo'>45.995097<!-- -->°,<!-- -->125.985003<!-- -->°<br></p><p class='caption overview-source'>Maxar<br></p><div class='meta-btns'><p class='caption daily-links shop'>Shop</p><p class='caption daily-links'><a href='mailto:?subject=Check out this post on Overview&amp;body=Check out the Pingyuan Reservoir post on Overview: https://www.over-view.com/overviews/pingyuan-reservoir' rel='noopener noreferrer' target='_blank'>Email</a>|<a href='https://www.facebook.com/sharer/sharer.php?u=https://www.over-view.com/overviews/pingyuan-reservoir' rel='noopener noreferrer' target='_blank'>FB</a></p></div></div>

count_posts = 0
# total_posts = []
while True:
    # posts_content, posts_links, posts
    # for content_html in soup.findAll('div', class_='daily__OverviewContent-sc-7emf19-4 ebZhgG'):
    #     soup_content = BeautifulSoup(str(content_html), 'lxml')

    #     post['post_header'] = soup_content.find('h1', class_ ='subheader daily-header').text
    #     post['post_text']   = soup_content.find('p',  class_ ='body-copy-small overview-description').text
    #     post['coordinates'] = soup_content.find('p',  class_ ='caption overview-geo').text
    #     post['posted']      = False

    #     sys.exit()



    for link_html in soup.findAll('div', class_='daily__OverviewImg-sc-7emf19-5 eAIJgU'):
        soup_link = BeautifulSoup(str(link_html), 'lxml')
        
        url = soup_link.find('a', href=True)['href']

        url_without_params = url.split('?')[0]
        url_with_proper_params = url_without_params + "?w=1920&h=1080&fm=jpg"
        print(url_with_proper_params)

        # url = 'https://www.datocms-assets.com/12893/1594948710-pingyuan-reservoir.jpg?w=1920&h=1080&fm=jpg'
        response = requests.get(url_without_params, stream=True)


        filename = url_without_params.split('/')[-1]
        filepath = "/home/ymka/" + filename
        print(filepath)

        with open(filepath, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)


        sys.exit()
        # for a in soup_link.find_all('a', href = True):
        #     if a.text:
        #         print(a['href'])
        # print(soup_link.find('a', href=True).text)



    # driver.find_element_by_xpath('//*[@id='w-node-e4d10996b7f3-c6b3f613']/a').click()
    # soup = BeautifulSoup(driver.page_source, 'lxml")
    # time.sleep(5)

