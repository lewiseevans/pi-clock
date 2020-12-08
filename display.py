import unicornhathd
import time

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

# Get the width and height of the display
width, height = unicornhathd.get_shape()

# Select font and size
FONT = ('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 10)


def display(hour, minute):
    unicornhathd.rotation(90)
    unicornhathd.brightness(0.3)

    colour = chooseColour(hour)

    drawTime(convertToStr(hour), 4, 2, colour)
    drawTime(convertToStr(minute), 4, 9, colour)
    unicornhathd.show()
    time.sleep(0.04)


def drawTime(time, xOffset, yOffset, colour):
    font_file, font_size = FONT
    font = ImageFont.truetype(font_file, font_size)

    text_width, text_height = font.getsize(time)

    image = Image.new('RGB', (text_width, text_height), (0, 0, 0))

    draw = ImageDraw.Draw(image)

    draw.text((0, 0), time, fill=colour, font=font)

    for x in range(text_width):
        for y in range(text_height):
            # Get the image pixel colour
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]

            # Position it on screen
            unicornhathd.set_pixel(
                width - 1 - x - xOffset, y - yOffset, r, g, b)


def convertToStr(time):
    timeStr = ""
    if time < 10:
        timeStr += "0"

    timeStr += str(time)

    return timeStr


def chooseColour(hour):

    colour = (255, 0, 0)

    if hour < 19 and hour > 8:
        colour = (255, 255, 255)

    return colour
