import zoneinfo
from datetime import datetime

paris = zoneinfo.ZoneInfo("Europe/Paris")
time_in_paris = datetime.now(paris)
print(f"Time in Paris:\n {time_in_paris}")

london = zoneinfo.ZoneInfo("Europe/London")
time_in_london = datetime.now(london)
print(f"Time in London:\n {time_in_london}")

hong_kong = zoneinfo.ZoneInfo("Asia/Hong_Kong")
time_in_hong_kong = datetime.now(hong_kong)
print(f"Time in Hong Kong:\n {time_in_hong_kong}")

nairobi = zoneinfo.ZoneInfo("Africa/Nairobi")
time_in_nairobi = datetime.now(nairobi)
print(f"Time in Nairobi:\n {time_in_nairobi}")
