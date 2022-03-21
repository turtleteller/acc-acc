import time
import os
import math
import datetime
import keyboard
from asciicanvas import AsciiCanvas

BORDER_CHARACTER = '?'
FILL_CHARACTER = '*'
HAND_CHARACTER_HOUR = ' '
HAND_CHARACTER_MIN = ' '
HAND_CHARACTER_SECOND = ' '



def draw_second_hand(ascii_canvas, seconds, length, fill_char):
    """
    Draw second hand
    """
    x0 = int(math.ceil(ascii_canvas.cols / 2.0))
    y0 = int(math.ceil(ascii_canvas.lines / 2.0))
    x1 = x0 + int(math.cos((seconds + 45) * 6 * math.pi / 180) * length * x_scale_ratio)
    y1 = y0 + int(math.sin((seconds + 45) * 6 * math.pi / 180) * length)
    ascii_canvas.add_line(int(x0), int(y0), int(x1), int(y1), fill_char=HAND_CHARACTER_SECOND)


def draw_minute_hand(ascii_canvas, minutes, length, fill_char):
    """
    Draw minute hand
    """
    x0 = int(math.ceil(ascii_canvas.cols / 2.0))
    y0 = int(math.ceil(ascii_canvas.lines / 2.0))
    x1 = x0 + int(math.cos((minutes + 45) * 6 * math.pi / 180) * length * x_scale_ratio)
    y1 = y0 + int(math.sin((minutes + 45) * 6 * math.pi / 180) * length)
    ascii_canvas.add_line(int(x0), int(y0), int(x1), int(y1), fill_char=HAND_CHARACTER_MIN)


def draw_hour_hand(ascii_canvas, hours, minutes, length, fill_char):
    """
    Draw hour hand
    """
    x0 = int(math.ceil(ascii_canvas.cols / 2.0))
    y0 = int(math.ceil(ascii_canvas.lines / 2.0))
    total_hours = hours + minutes / 60.0
    x1 = x0 + int(math.cos((total_hours + 45) * 30 * math.pi / 180) * length * x_scale_ratio)
    y1 = y0 + int(math.sin((total_hours + 45) * 30 * math.pi / 180) * length)
    ascii_canvas.add_line(int(x0), int(y0), int(x1), int(y1), fill_char=HAND_CHARACTER_HOUR)


def draw_clock_face(ascii_canvas, radius, mark_char):
    """
    Draw clock face with hour and minute marks
    """
    x0 = ascii_canvas.cols // 2
    y0 = ascii_canvas.lines // 2
    # draw marks first
    for mark in range(1, 12 * 5 + 1):
        x1 = x0 + int(math.cos((mark + 45) * 6 * math.pi / 180) * radius * x_scale_ratio)
        y1 = y0 + int(math.sin((mark + 45) * 6 * math.pi / 180) * radius)
        if mark % 5 != 0:
            ascii_canvas.add_text(x1, y1, mark_char)
    # start from 1 because at 0 index - 12 hour
    for mark in range(1, 12 + 1):
        x1 = x0 + int(math.cos((mark + 45) * 30 * math.pi / 180) * radius * x_scale_ratio)
        y1 = y0 + int(math.sin((mark + 45) * 30 * math.pi / 180) * radius)
        ascii_canvas.add_text(x1, y1, '%s' % mark)


def draw_clock(cols, lines, now):
    """
    Draw clock
    """
    if cols < 25 or lines < 25:
        print('Too little columns/lines for print out the clock!')
        exit()
    # prepare chars
    single_line_border_chars = ('.', '-', '.', '|', ' ', '|', '`', '-', "'")
    second_hand_char = '.'
    minute_hand_char = 'o'
    hour_hand_char = 'O'
    mark_char = '`'
    if os.name == 'nt':
        single_line_border_chars = ('.', '-', '.', '|', ' ', '|', '`', '-', "'")  # ('\xDA', '\xC4', '\xBF', '\xB3', '\x20', '\xB3', '\xC0', '\xC4', '\xD9')
        second_hand_char = '.'  # '\xFA'
        minute_hand_char = 'o'  # '\xF9'
        hour_hand_char = 'O'  # 'o'
        mark_char = '`'  # '\xF9'
    # create ascii canvas for clock and eval vars
    ascii_canvas = AsciiCanvas(cols, lines)
    center_x = int(math.ceil(cols / 2.0))
    center_y = int(math.ceil(lines / 2.0))
    radius = center_y - 5
    second_hand_length = int(radius / 1.17)
    minute_hand_length = int(radius / 1.25)
    hour_hand_length = int(radius / 1.95)
    # add clock region and clock face
    ascii_canvas.add_rect(5, 3, int(math.floor(cols / 2.0)) * 2 - 9, int(math.floor(lines / 2.0)) * 2 - 5, FILL_CHARACTER, BORDER_CHARACTER)
    draw_clock_face(ascii_canvas, radius, mark_char)
    # add regions with weekday and day if possible
	
    seconds = time.strftime('%S', time.localtime(now))
    minutes = time.strftime('%M', time.localtime(now))
    hours = time.strftime('%H', time.localtime(now))

    firstText = 'No'
    secondText = 'No'

    if hours == '16' and minutes == '24':
      firstText = 'Yes'
      secondText = 'Yes'
      os.system('color B')

    if center_x > 25:
        left_pos = int(radius * x_scale_ratio) / 2 - 10
        ascii_canvas.add_nine_patch_rect(int(center_x + left_pos), int(center_y - 1), 5, 3, single_line_border_chars)
        ascii_canvas.add_text(int(center_x + left_pos + 1), int(center_y), firstText)
        ascii_canvas.add_nine_patch_rect(int(center_x + left_pos + 5), int(center_y - 1), 4, 3, single_line_border_chars)
        ascii_canvas.add_text(int(center_x + left_pos + 1 + 20), int(center_y), secondText)
    # add clock hands
    draw_second_hand(ascii_canvas, int(seconds), second_hand_length, fill_char=second_hand_char)
    draw_minute_hand(ascii_canvas, int(minutes), minute_hand_length, fill_char=minute_hand_char)
    draw_hour_hand(ascii_canvas, int(hours), int(minutes), hour_hand_length, fill_char=hour_hand_char)
    # print out canvas
    ascii_canvas.print_out()


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


while True:
# loop forever

  # We have time in seconds. So we add one second. Convert it to object, then from object to a readable string 

  timeResultSeconds = globalTime + 1 # +1 second to current time (as normal manual clock)
  timeResultObject = time.localtime(timeResultSeconds) # .localtime converts time in second to time 'object'

  result = time.strftime("%H:%M:%S", timeResultObject) # .strftime formats the date from object, to a readable string
  os.system('clear') # erase clock in terminal everytime function is looping

  print(result)
  globalTime = timeResultSeconds

  time.sleep(sleepDuration)



