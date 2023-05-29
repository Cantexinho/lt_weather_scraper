from datetime import datetime, timedelta

MAX_DATE = datetime.now() + timedelta(days=6)

VILNIUS_PAGES = {
    "timeanddate": "https://www.timeanddate.com/weather/lithuania/vilnius/ext",
    "metoffice": "https://www.metoffice.gov.uk/weather/forecast/u99zpk026#",
    "weather": "https://weather.com/weather/tenday/l/82308b95495a32864bc9cd5f4815c86946c990d246f6a521f2579b92b648ac52",
}

KAUNAS_PAGES = {
    "timeanddate": "https://www.timeanddate.com/weather/lithuania/kaunas/ext",
    "metoffice": "https://www.metoffice.gov.uk/weather/forecast/u9bbnr4yk#",
    "weather": "https://weather.com/weather/tenday/l/18638f270f9b33bb82c1e2751e506ae731aceeea03c2cd0dfc98dd3212946ed0",
}
