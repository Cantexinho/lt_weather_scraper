import requests
from bs4 import BeautifulSoup


class MetofficeScraper:
    def __init__(self, date: str) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        self.url = (
            f"https://www.metoffice.gov.uk/weather/forecast/u99zpk026#?date={date}"
        )
        self.soup = None

    def fetch_page(self):
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, "html.parser")

    def get_sunrise_time(self) -> str:
        sunrise_div_tag = self.soup.find("div", class_="weather-text sunrise-sunset")
        return sunrise_div_tag.find("time").string

    def get_sunset_time(self) -> str:
        sunset_div_tag = self.soup.find(
            "div", class_="weather-text sunrise-sunset sunset"
        )
        return sunset_div_tag.find("time").string

    def get_high_temperature(self) -> str:
        return self.soup.find("span", class_="tab-temp-high").get_text(strip=True)

    def get_low_temperature(self) -> str:
        return self.soup.find("span", class_="tab-temp-low").get_text(strip=True)
