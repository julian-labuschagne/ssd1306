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

while True:

    now = datetime.datetime.now()
    weekday = now.strftime("%A")
    day = now.strftime("%d")
    month = now.strftime("%B")
    w, h = draw.textsize(weekday, titleFont)

    print("Width     : {}".format(width))
    print("Text      : {}".format(w))
    print("Res       : {}".format((int(width - w))))

    draw.rectangle(( 0, 0, width -1, 18), outline=255, fill=0)
    draw.text((int((width -1 - w) / 2), 2), "{}".format(weekday), font=titleFont, fill=255)
    # draw.text((10, 16), "22:00", font=clockFont, fill=255)
    # draw.text((10, 16), "W: {}".format(width), font=font, fill=255)
    # draw.text((10, 32), "w: {}".format(w), font=font, fill=255)
    # draw.text((10, 48), "P: {}".format(int((width - w) / 2)), font=font, fill=255)

    w, h = draw.textsize(day, titleFont)
    draw.text((int((width -1 - w) / 2), 20), "{}".format(day), font=clockFont, fill=255)

    draw.rectangle((0, height - 1 - 18, width -1, height -1), outline=255, fill=0)

    w, h = draw.textsize(month, titleFont)
    draw.text((int((width -1 - w) / 2), height -1 - 16), "{}".format(month), font=titleFont, fill=255)
    # draw.text((0, 52), "{}".format(weekday), font=titleFont, fill=0)


    disp.image(image)
    disp.display()

    time.sleep(.1)
