import datetime as date_objects
from datetime import datetime

kati = datetime.now()  # preferred way
utc_now = datetime.utcnow()

print(kati, utc_now, sep="\n")
