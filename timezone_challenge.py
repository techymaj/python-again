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
    tz = zoneinfo.ZoneInfo(timezone)
    time_in_city = datetime.now(tz=tz)

    print(f"Time in {major_city}:")
    short_time = time_in_city.strftime("%H:%M:%S")
    zone = time_in_city.tzname()
    print_ic(f"{short_time} - " f"{zone}", BLUE)


for each_city in timezones:
    print_timezone(each_city, timezones[each_city])
