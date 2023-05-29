from datetime import datetime
from config import MAX_DATE


def is_valid_date(req_date: datetime) -> bool:
    if req_date > MAX_DATE:
        print("Date too big!")
        return False
    return True


def print_data(received_data: dict, req_date: datetime, req_city: str) -> None:
    print("City: ", req_city)
    print("Date: ", req_date.date())
    for single_data in received_data:
        print(single_data, received_data[single_data])
