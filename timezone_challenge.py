import zoneinfo
from datetime import datetime

from color_codes import print_ic, BLUE

timezones = {
    "Paris": "Europe/Paris",
    "London": "Europe/London",
    "Hong_Kong": "Asia/Hong_Kong",
    "Nairobi": "Africa/Nairobi",
}

def print_timezone(major_city: str, timezone: str) -> None:
    city = zoneinfo.ZoneInfo(timezone)
    time_in_city = datetime.now(city).strftime("%H:%M:%S")
    print(f"Time in {major_city}:")
    print_ic(f"{time_in_city}", BLUE)


for each_city in timezones:
    print_timezone(each_city, timezones[each_city])
