from bs4 import BeautifulSoup

def parse_post_body_from_html(content_html):
    soup_content = BeautifulSoup(str(content_html), 'lxml')

    post = {}

    post['post_header'] = soup_content.find('h1', class_ ='subheader daily-header').text
    post['post_text']   = soup_content.find('p',  class_ ='body-copy-small overview-description').text
    post['coordinates'] = soup_content.find('p',  class_ ='caption overview-geo').text
    post['posted']      = False

    return post

def parse_link_from_html(link_html, img_params):
    soup_link = BeautifulSoup(str(link_html), 'lxml')
    
    url = soup_link.find('a', href=True)['href']

    url_without_params = url.split('?')[0]
    url_with_proper_params = url_without_params + "?" + img_params

    return [url_without_params, url_with_proper_params]



def get_link_info(url_without_params, img_storage):
    filename = url_without_params.split('/')[-1]
    path_to_image = img_storage + filename
    epoch_id = filename.split('-')[0]

    return [path_to_image, epoch_id]