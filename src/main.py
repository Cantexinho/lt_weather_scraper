from modules.metoffice_scraper import MetofficeScraper
from datetime import datetime, timedelta


def get_metoffice_data(req_date: datetime) -> dict:
    metoffice = MetofficeScraper(req_date.strftime("%Y-%m-%d"))
    metoffice.fetch_page()
    weather_data = {}

    weather_data["temp_high"] = metoffice.get_high_temperature()
    weather_data["temp_low"] = metoffice.get_low_temperature()
    weather_data["sunrise"] = metoffice.get_sunrise_time()
    weather_data["sunset"] = metoffice.get_sunset_time()
    return weather_data


def main():
    max_date = datetime.now() + timedelta(days=6)
    req_date = datetime(2023, 6, 2)

    if req_date > max_date:
        print("Date too big!")
        return

    metoffice_data = get_metoffice_data(req_date)
    print(metoffice_data)


if __name__ == "__main__":
    main()
