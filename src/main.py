from data.weather import get_weather_data_concurrently
from datetime import datetime
from config import MAX_DATE


def main():
    req_date = datetime(2023, 5, 29)
    if req_date > MAX_DATE:
        print("Date too big!")
        return

    print("date: ", req_date.date())
    received_data = get_weather_data_concurrently(req_date)
    for single_data in received_data:
        print(single_data, received_data[single_data])


if __name__ == "__main__":
    main()
