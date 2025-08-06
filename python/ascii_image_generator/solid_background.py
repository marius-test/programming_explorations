from PIL import Image, ImageDraw, ImageFont
import pyfiglet

ascii_art = pyfiglet.figlet_format("Melanie")

img_width = 1080
img_height = 1920

img = Image.new("RGB", (img_width, img_height), color=(24, 62, 125))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(r"C:\\Windows\\Fonts\\courbd.ttf", 24)

ascent, descent = font.getmetrics()
line_height = ascent + descent

lines = ascii_art.split('\n')
total_text_height = line_height * len(lines)
y_text = (img_height - total_text_height) // 2

for line in lines:
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]  # width from bounding box
    x_text = (img_width - line_width) // 2
    draw.text((x_text, y_text), line, font=font, fill=(249, 249, 249))
    y_text += line_height

img.save("ascii_vertical_wallpaper.png")
