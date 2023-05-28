import requests
from bs4 import BeautifulSoup


class MetofficeScraper:
    def __init__(self, date: str) -> None:
        self.url = f"https://www.metoffice.gov.uk/weather/forecast/u99zpk026#"
        self.date = date
        self.soup = self.fetch_page()

    def fetch_page(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    def get_sunrise_time(self) -> str:
        req_date_tag = self.soup.find("li", attrs={"data-tab-id": self.date})
        sunrise_div_tag = req_date_tag.find("div", class_="weather-text sunrise-sunset")
        return sunrise_div_tag.find("time").string

    def get_sunset_time(self) -> str:
        req_date_tag = self.soup.find("li", attrs={"data-tab-id": self.date})
        sunset_div_tag = req_date_tag.find(
            "div", class_="weather-text sunrise-sunset sunset"
        )
        return sunset_div_tag.find("time").string

    def get_high_temperature(self) -> str:
        req_date_tag = self.soup.find("li", attrs={"data-tab-id": self.date})
        return req_date_tag.find("span", class_="tab-temp-high").get_text(strip=True)

    def get_low_temperature(self) -> str:
        req_date_tag = self.soup.find("li", attrs={"data-tab-id": self.date})
        return req_date_tag.find("span", class_="tab-temp-low").get_text(strip=True)
