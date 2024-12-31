import datetime as date_objects
from datetime import datetime

today = datetime.today()
kati = datetime.now()
utc_now = datetime.utcnow()
_time = date_objects.time.fromisoformat("11:30")

print(today, _time, kati, utc_now, sep="\n")
