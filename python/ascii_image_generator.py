from PIL import Image, ImageDraw, ImageFont
import pyfiglet

ascii_art = pyfiglet.figlet_format("NASA")

img_width = 1080
img_height = 1920

img = Image.new("RGB", (img_width, img_height), color="black")
draw = ImageDraw.Draw(img)

# load font
font = ImageFont.truetype(r"C:\\Windows\\Fonts\\cour.ttf", 24)

ascent, descent = font.getmetrics()
line_height = ascent + descent

lines = ascii_art.split('\n')
total_text_height = line_height * len(lines)
y_text = (img_height - total_text_height) // 2

for line in lines:
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]  # width from bounding box
    x_text = (img_width - line_width) // 2
    draw.text((x_text, y_text), line, font=font, fill="white")
    y_text += line_height

img.save("nasa_ascii_wallpaper.png")
