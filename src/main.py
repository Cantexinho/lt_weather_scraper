from modules.metoffice_scraper import MetofficeScraper
from modules.timeanddate_scraper import TimeAndDateScraper
from modules.weather_scraper import WeatherScraper
from datetime import datetime, timedelta


def get_metoffice_data(req_date: datetime) -> dict:
    metoffice = MetofficeScraper(req_date.strftime("%Y-%m-%d"))
    weather_data = {}

    weather_data["temp_high"] = metoffice.get_high_temperature()
    weather_data["temp_low"] = metoffice.get_low_temperature()
    weather_data["sunrise"] = metoffice.get_sunrise_time()
    weather_data["sunset"] = metoffice.get_sunset_time()
    return weather_data


def get_timeanddate_data(req_date: datetime) -> dict:
    timeanddate = TimeAndDateScraper(req_date.strftime("%#d %b"))
    weather_data = {}

    weather_data["temp_high"] = timeanddate.get_high_temperature()
    weather_data["temp_low"] = timeanddate.get_low_temperature()
    weather_data["sunrise"] = timeanddate.get_sunrise_time()
    weather_data["sunset"] = timeanddate.get_sunset_time()
    return weather_data


def get_weather_data(req_date: datetime) -> dict:
    if datetime.now() >= req_date:
        return
    weather_scraper = WeatherScraper(req_date.strftime("%d"))
    weather_data = {}

    weather_data["temp_high"] = weather_scraper.get_high_temperature()
    weather_data["temp_low"] = weather_scraper.get_low_temperature()
    return weather_data


def main():
    max_date = datetime.now() + timedelta(days=6)
    req_date = datetime(2023, 5, 28)

    if req_date > max_date:
        print("Date too big!")
        return

    metoffice_data = get_metoffice_data(req_date)
    timeanddate_data = get_timeanddate_data(req_date)
    weather_data = get_weather_data(req_date)
    print("date: ", req_date.date())
    print(metoffice_data, "\n", timeanddate_data, "\n", weather_data)


if __name__ == "__main__":
    main()
