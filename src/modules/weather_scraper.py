import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class WeatherScraper:
    def __init__(self, date: str, url: str) -> None:
        self.url = url
        self.date = date
        self.soup = self.fetch_page()
        self.summary_tag = self.get_summary_tag()

    def fetch_page(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return round(celsius)

    def get_summary_tag(self) -> Tag:
        h3_tag = self.soup.find_all("h3", class_="DetailsSummary--daypartName--kbngc")
        for tag in h3_tag:
            if self.date in tag.text:
                return tag.find_parent("summary")

    def get_high_temperature(self) -> str:
        farenheit_temp = self.summary_tag.find(
            "span", {"data-testid": "TemperatureValue"}
        ).get_text()
        farenheit_int = int(
            "".join(digit for digit in farenheit_temp if digit.isdigit())
        )
        return self.fahrenheit_to_celsius(farenheit_int)
        return

    def get_low_temperature(self) -> str:
        farenheit_temp = self.summary_tag.find(
            "span", {"data-testid": "lowTempValue"}
        ).get_text()
        farenheit_int = int(
            "".join(digit for digit in farenheit_temp if digit.isdigit())
        )
        return self.fahrenheit_to_celsius(farenheit_int)
