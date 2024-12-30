import datetime
import locale

locale.setlocale(locale.LC_ALL, "fr_FR.utf-8")

# today = datetime.datetime.now()
today = datetime.date.today()
print(f"Today is {today}")

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime("%A the %d of %B, %Y")
print(pretty_start)
