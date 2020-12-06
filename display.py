import unicornhathd
import time

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

# Get the width and height of the display
width, height = unicornhathd.get_shape()

# Select font and size
FONT = ('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 12)


def display(hour):

    unicornhathd.rotation(90)
    unicornhathd.brightness(0.3)

    font_file, font_size = FONT

    font = ImageFont.truetype(font_file, font_size)

    text_width, text_height = font.getsize(hour)

    text_width += width + 1

    image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))

    draw = ImageDraw.Draw(image)

    draw.text((1, 2), hour, fill=(255, 0, 0), font=font)

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]
            unicornhathd.set_pixel(width-1-x, y, r, g, b)

    unicornhathd.show()
    time.sleep(0.04)
