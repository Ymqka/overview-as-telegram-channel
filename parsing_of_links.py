from parser import parse_article

from selenium import webdriver


# Это пока очень сырой код, но работает


path = r"/home/kirill/Desktop/Coding/Python/overview-as-telegram-channel/geckodriver"
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.over-view.com/digital-index/?page=1&configure%5BhitsPerPage%5D=30')
soup = BeautifulSoup(driver.page_source, "lxml")

rows = soup.select("ul.ais-Hits-list > li > a")

overview_links = []
for row in rows:
    overview_links.append(row.get('href'))

for url in overview_links:
    url = "https://www.over-view.com/" + url
    parse_article(url)

print("hello")
