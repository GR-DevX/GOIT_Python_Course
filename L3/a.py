import datetime as dt
from datetime import datetime as dtdt, timedelta as td, timezone as tz
dt1=dtdt(1995, 4, 7, hour=12, minute=30, second=13)
dt2=dtdt(2005, 4, 7, hour=12, minute=30, second=13)
td1=td(days=36, minutes=150)
# print(td1)
# print(type(dt2-dt1))
# print(dt2+td1)
now=dtdt.now()
# print(now)
# ts1=dtdt.timestamp(dtdt.now())
# print(ts1)
# print(dtdt.fromtimestamp(ts1))
#print(now)
udow={
    0:'понеділок',
    1:'вівторок',
    2:'середа',
    3:'четвер',
    4:'п’ятниця',
    5:'субота',
    6:'неділя',
    }
# print(dtdt.strftime(now,f"%y %b %d, {udow[now.weekday()]}, %I_%M_%S %p"))
# dt3=dtdt.strptime("01/03/1998, 12:30:45", "%d/%m/%Y, %H:%M:%S")
# print(dt3)
# print(type(dt3))
# print(now.isoformat())
# print(dtdt.fromisoformat("2024-12-19T08:30:00.000000"))
# print(dt1)
# print(dt2)
# print(dir(td))
tz1=tz(td(hours=2),'UTC+2')
dt1=dtdt(1995, 4, 7, hour=12, minute=30, second=13, tzinfo=tz1)
print(dt1.isoformat())
print(dtdt.today())
print(dtdt.now(tz1))

