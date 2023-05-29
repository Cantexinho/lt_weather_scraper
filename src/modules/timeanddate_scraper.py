import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class TimeAndDateScraper:
    def __init__(self, date: str, url: str) -> None:
        self.headers = {
            "Accept-Language": "en-US,en;q=0.9",
        }
        self.date = date
        self.url = url
        self.soup = self.fetch_page()
        self.req_tr_tag = self.get_req_tr_tag()

    def fetch_page(self):
        response = requests.get(self.url, headers=self.headers)
        return BeautifulSoup(response.text, "html.parser")

    def get_req_tr_tag(self) -> Tag:
        tr_tags = self.soup.find_all("tr")
        for tr in tr_tags:
            th_tag = tr.find("th")
            if th_tag and self.date in th_tag.text:
                return tr

    def get_sunrise_time(self) -> str:
        return self.req_tr_tag.find_all("td")[-2].text.strip()

    def get_sunset_time(self) -> str:
        return self.req_tr_tag.find_all("td")[-1].text.strip()

    def get_high_temperature(self) -> str:
        temperatures = self.req_tr_tag.find_all("td")[1].text.strip()
        return temperatures.split(" ")[0] + "°"

    def get_low_temperature(self) -> str:
        temperatures = self.req_tr_tag.find_all("td")[1].text.strip()
        return temperatures.split(" ")[2].split("\xa0")[0] + "°"
