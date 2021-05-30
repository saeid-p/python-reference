# Python 3.2+ has support for %z format when parsing a string into a datetime object.
# For other versions of Python, you can use an external library such as 'dateutil'.

from datetime import datetime, timedelta, timezone

dt1 = datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")

now = datetime.now()
then = datetime(2016, 5, 23)

#### Date Delta ####
delta = now - then

print(delta.days)
print(delta.seconds)
print(delta.microseconds)

date_n_days_after = now + timedelta(days = 5)
date_n_days_before = now - timedelta(days = 5)

#### Format to String ####
date_format = "%d %B %Y" # Reference: https://strftime.org/
print(now.strftime(date_format))

#### Date Only ####
today = datetime.date.today()
new_year = datetime.date(2017, 1, 1)

#### Time Only ####
noon = datetime.time(12, 0, 0)

#### Timestamp ####
# The datetime module can convert a POSIX timestamp to a ITC datetime object.
# The Epoch is January 1st, 1970 midnight.

import time
from datetime import datetime

seconds_since_epoch=time.time() #1469182681.709
utc_date = datetime.utcfromtimestamp(seconds_since_epoch)

#### Time Zones ####
CSTZone = timezone(timedelta(hours = -8))
dt2 = datetime(2015, 1, 1, 12, 0, 0, tzinfo = CSTZone)

print(dt2) # 2015-01-01 12:00:00-08:00
print(dt2.tzname()) # UTC-08:00

# For zones with daylight savings time, python standard libraries do not provide a standard class.
# 'pytz' and 'dateutil' are popular libraries providing time zone classes.
# https://dateutil.readthedocs.io/en/stable/tz.html