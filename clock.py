import time
import os
import math
import datetime
import keyboard

globalTime = time.time() # current time in seconds (eg. 1647790151.79)
sleepDuration = 1.0 # clock updates every second
count = 0 # number of time the key is pressed

def speedUp(param):

  global sleepDuration, count
  if count > 50:
  # not going faster
    return

  newSleepDuration = sleepDuration * 0.9 # clock update time is shorten
  count += 1
  sleepDuration = round(newSleepDuration, 8) # 8 number after decimal

keyboard.on_press_key("p", speedUp) # Press key 'p' to count +1

def slowDown(param):

  global sleepDuration, count
  if count > 50:
  # not going slower
    return

  newSleepDuration = sleepDuration / 0.9 # clock update time is longer
  count += 1
  sleepDuration = round(newSleepDuration, 8) # 8 number after decimal

keyboard.on_press_key("x", slowDown) # Press key 'p' to count +1

while True:
# loop forever

  # We have time in seconds. So we add one second. Convert it to object, then from object to a readable string 

  timeResultSeconds = globalTime + 1 # +1 second to current time (as normal manual clock)
  timeResultObject = time.localtime(timeResultSeconds) # .localtime converts time in second to time 'object'

  result = time.strftime("%H:%M:%S", timeResultObject) # .strftime formats the date from object, to a readable string
  #clear() # erase clock in terminal everytime function is looping
  os.system('clear')

  print("\n")
  print("******** FAGE NOT POUND")
  print("\n")
  print("*************************************************") 
  print("*************************************************")
  print("*************************************************")
  print("******** " + result + " ACCACC")
  print("*************************************************")
  print("*************************************************")
  print("*************************************************")
  print("\n") 
  print("*************************************************")
  print("*************************************************")
  print("******** 18:00:00" + " ACCACC  OPENING")
  print("******** 04:00:00" + " ACCACC  DISCUSSION WITH PLATFORM BK")
  print("******** 10:00:00" + " ACCACC  LOOTBOX REVEAL")
  print("******** 00:00:00" + " ACCACC  CLOSING")
  print("*************************************************")
  print("*************************************************")

  globalTime = timeResultSeconds

  time.sleep(sleepDuration)



