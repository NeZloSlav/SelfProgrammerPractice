from urllib import request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all("a"):
            url = BeautifulSoup.get(tag, "href")
            if url is None:
                continue
            print(url)


news = "https://news.google.ru/"
Scraper(news).scrape()
