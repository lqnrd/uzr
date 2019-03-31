#UZR - Universal Realtime Zone
#requires python 3

import sys
import time
import shutil #for terminal width
import datetime
import calendar

TERMINAL_WIDTH, _ = shutil.get_terminal_size()

t = time.localtime()
localOffsetSeconds = calendar.timegm(t) - calendar.timegm(time.gmtime(time.mktime(t)))
if t.tm_isdst:
  localOffsetSeconds -= 3600 #get base offset without DST
if len(sys.argv) >= 2:
  localOffsetSeconds = int(sys.argv[1])
print("UZR - Universal Realtime Zone (%d seconds offset)" % localOffsetSeconds)

def getUZR(offsetSeconds = 0):
  n = datetime.datetime.now(datetime.timezone.utc)
  n += datetime.timedelta(0, offsetSeconds)
  if (n.month == 3) and (n.day >= 2) and (n.day <= 31):
    n += datetime.timedelta(0, (n.day - 1)*2*60) #03/02: add 2 minutes ... 03/31: add 60 minutes
  elif (n.month >= 4) and (n.month <= 10):
    n += datetime.timedelta(0, 3600) #usual DST
  return n

def getTimeString(nDateTime):
  return nDateTime.strftime("%Y-%m-%d %H:%M:%S")

def rprint_trim(text):
  print((text + " " * TERMINAL_WIDTH)[:TERMINAL_WIDTH-1], end="\r") #python 2.7: "print(...),"
while True:
  rprint_trim(getTimeString(datetime.datetime.now()) + " - " + getTimeString(datetime.datetime.now(datetime.timezone.utc)) + " UTC - " + getTimeString(getUZR(localOffsetSeconds)) + " UZR")
  time.sleep(1)
