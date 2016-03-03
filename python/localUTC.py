import datetime
from time import strftime, localtime
utc=datetime.datetime.utcnow()
print utc.strftime('%H:%M')
print strftime('%H:%M',localtime())
