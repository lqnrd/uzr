#UZR - Universal Realtime Zone
#needs python 3+

import sys
import time
import shutil #for terminal width
import datetime

TERMINAL_WIDTH, _ = shutil.get_terminal_size()

def getTimeString(sZone = "UZR"):
  if sZone == "HERE":
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  if sZone == "UTC":
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
  n = datetime.datetime.now(datetime.timezone.utc)
  n += datetime.timedelta(0, 3600) #UTC+1
  if (n.month == 3) and (n.day >= 2) and (n.day <= 31):
    n += datetime.timedelta(0, (n.day - 1)*2*60) #03/02: add 2 minutes ... 03/31: add 60 minutes
  elif (n.month >= 4) and (n.month <= 10):
    n += datetime.timedelta(0, 3600) #usual CEST
  return n.strftime("%Y-%m-%d %H:%M:%S")

def rprint_trim(text):
  print((text + " " * TERMINAL_WIDTH)[:TERMINAL_WIDTH-1], end="\r") #python 2.7: "print(...),"
while True:
  rprint_trim(getTimeString("HERE") + " - " + getTimeString("UTC") + " UTC - " + getTimeString() + " UZR")
  time.sleep(1)

#rprint_trim(getTimeString("HERE") + " - " + getTimeString("UTC") + " UTC - " + getTimeString() + " UZR")
