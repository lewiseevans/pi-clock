import unicornhathd
import time

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

# Get the width and height of the display
width, height = unicornhathd.get_shape()

# Select font and size
FONT = ('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 8)


def display(hour, minute):

    unicornhathd.rotation(180)
    unicornhathd.brightness(0.3)

    font_file, font_size = FONT

    font = ImageFont.truetype(font_file, font_size)

    text_width, text_height = font.getsize(hour)

    image = Image.new('RGB', (text_width, text_height), (0, 0, 0))

    draw = ImageDraw.Draw(image)

    draw.text((0, 0), hour, fill=(255, 0, 0), font=font)

    for x in range(text_width):
        for y in range(text_height):
            # Get the image pixel colour
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]

            # Position it on screen
            unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

    unicornhathd.show()
    time.sleep(0.04)
