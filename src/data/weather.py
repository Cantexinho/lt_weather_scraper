from modules.metoffice_scraper import MetofficeScraper
from modules.timeanddate_scraper import TimeAndDateScraper
from modules.weather_scraper import WeatherScraper
from datetime import datetime
import threading
from config import VILNIUS_PAGES, KAUNAS_PAGES


def get_metoffice_data(req_date: datetime, city_url: str) -> dict:
    metoffice = MetofficeScraper(req_date.strftime("%Y-%m-%d"), city_url)
    weather_data = {}

    weather_data["temp_high"] = metoffice.get_high_temperature()
    weather_data["temp_low"] = metoffice.get_low_temperature()
    weather_data["sunrise"] = metoffice.get_sunrise_time()
    weather_data["sunset"] = metoffice.get_sunset_time()
    return weather_data


def get_timeanddate_data(req_date: datetime, city_url: str) -> dict:
    timeanddate = TimeAndDateScraper(req_date.strftime("%#d %b"), city_url)
    weather_data = {}

    weather_data["temp_high"] = timeanddate.get_high_temperature()
    weather_data["temp_low"] = timeanddate.get_low_temperature()
    weather_data["sunrise"] = timeanddate.get_sunrise_time()
    weather_data["sunset"] = timeanddate.get_sunset_time()
    return weather_data


def get_weather_data(req_date: datetime, city_url) -> dict:
    if datetime.now() >= req_date:
        return
    weather_scraper = WeatherScraper(req_date.strftime("%d"), city_url)
    weather_data = {}

    weather_data["temp_high"] = weather_scraper.get_high_temperature()
    weather_data["temp_low"] = weather_scraper.get_low_temperature()
    return weather_data


def get_city_urls(city: str) -> dict:
    if city == "Vilnius":
        return VILNIUS_PAGES
    if city == "Kaunas":
        return KAUNAS_PAGES


def get_weather_data_concurrently(req_date: datetime, city: str) -> dict:
    weather_data = {}

    city_urls = get_city_urls(city)

    def _run_metoffice_data():
        weather_data["www.metoffice.gov.uk"] = get_metoffice_data(
            req_date, city_urls.get("metoffice")
        )

    def _run_timeanddate_data():
        weather_data["www.timeanddate.com"] = get_timeanddate_data(
            req_date, city_urls.get("timeanddate")
        )

    def _run_weather_data():
        weather_data["www.weather.com"] = get_weather_data(
            req_date, city_urls.get("weather")
        )

    thread1 = threading.Thread(target=_run_metoffice_data)
    thread2 = threading.Thread(target=_run_timeanddate_data)
    thread3 = threading.Thread(target=_run_weather_data)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    return weather_data
