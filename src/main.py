from data.weather import get_weather_data_concurrently
from utils.helper_functions import is_valid_date, print_data
from datetime import datetime


def main():
    req_date = datetime(2023, 12, 4)
    req_city = "Kaunas"
    if not is_valid_date(req_date):
        return
    received_data = get_weather_data_concurrently(req_date, req_city)
    print_data(received_data, req_date, req_city)


if __name__ == "__main__":
    main()
