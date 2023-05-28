from modules.metoffice_scraper import MetofficeScraper

if __name__ == "__main__":
    metoffice = MetofficeScraper("2023-05-28")
    metoffice.fetch_page()
    weather_data = {}

    weather_data["temp_high"] = metoffice.get_high_temperature()
    weather_data["temp_low"] = metoffice.get_low_temperature()
    weather_data["sunrise"] = metoffice.get_sunrise_time()
    weather_data["sunset"] = metoffice.get_sunset_time()

    print(weather_data)
