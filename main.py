import time
import datetime

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = 0
top = padding
bottom = height - padding

x = 0

font = ImageFont.load_default()
titleFont = ImageFont.truetype('Pixellari.ttf', 14)
clockFont = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf', 24)

def calendar_page():

    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Get the date variables to print
    now = datetime.datetime.now()
    weekday = now.strftime("%A")
    day = now.strftime("%d")
    month = now.strftime("%B")

    # Print some debug variables
    print("----------------")
    print("Weekday : {}".format(weekday))
    print("Day     : {}".format(day))
    print("Month   : {}".format(month))

    # Draw weekday
    w, h = draw.textsize(weekday, titleFont)
    draw.rectangle(( 0, 0, width -1, 18), outline=255, fill=0)
    draw.text((int((width -1 - w) / 2), 2), "{}".format(weekday), font=titleFont, fill=255)

    # Draw day
    w, h = draw.textsize(day, titleFont)
    draw.text((int((width -1 - w) / 2), 20), "{}".format(day), font=clockFont, fill=255)

    # Draw month
    draw.rectangle((0, height - 1 - 18, width -1, height -1), outline=255, fill=0)
    w, h = draw.textsize(month, titleFont)
    draw.text((int((width -1 - w) / 2), height -1 - 16), "{}".format(month), font=titleFont, fill=255)

    disp.image(image)
    disp.display()

def clock_digital():

    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Get the time variables to print
    now = datetime.datetime.now()
    hours = now.strftime("%I")
    minutes = now.strftime("%M")
    am_or_pm = now.strftime("%p")
    seconds = now.strftime("%S")
    weekday = now.strftime("%A").upper()
    day = now.strftime("%d")
    month = now.strftime("%b").upper()
    year = now.strftime("%Y")

    # Print some debug variables
    print("----------------")
    print("{}".format(weekday))
    print("Hours   : {}".format(hours))
    print("Minutes : {}".format(minutes))
    print("Minutes : {}".format(am_or_pm))
    print("Seconds : {}".format(seconds))
    print("Day     : {}".format(day))
    print("Month   : {}".format(month))
    print("Year    : {}".format(year))

    # Draw weekday
    titleFont = ImageFont.truetype('Pixellari.ttf', 16)
    w, h = draw.textsize(weekday, titleFont)
    draw.text((int((width -1 - w) / 2), 2), "{}".format(weekday), font=titleFont, fill=255)

    # Draw time
    w, h = draw.textsize("{}:{} {}".format(hours, minutes, am_or_pm), clockFont)
    # draw.rectangle(( 0, 0, width -1, 18), outline=255, fill=0)
    draw.text((int((width -1 - w) / 2), int((height -1 -h) / 2)), "{}:{} {}".format(hours, minutes, am_or_pm), font=clockFont, fill=255)

    # Draw month, day and year
    titleFont = ImageFont.truetype('Pixellari.ttf', 16)
    w, h = draw.textsize("{} {}".format(month, day), titleFont)
    draw.text((0, (height -1 - h)), "{} {}".format(month, day), font=titleFont, fill=255)
    w, h = draw.textsize("{}".format(year), titleFont)
    draw.text((width - 1 - w, (height -1 - h)), "{}".format(year), font=titleFont, fill=255)

    disp.image(image)
    disp.display()

while True:

    calendar_page()
    time.sleep(5)

    clock_digital()
    time.sleep(5)
