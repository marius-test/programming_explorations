from PIL import Image, ImageDraw, ImageFont
import pyfiglet
import math

# settings
text = "Melanie"
img_width = 1080
img_height = 1920
base_color = (24, 62, 125)  # dark blue
center_lightness_boost = 100  # how much lighter the center is

# create image
img = Image.new("RGB", (img_width, img_height))
center_x = img_width // 2
center_y = img_height // 2
max_dist = math.hypot(center_x, center_y)

# generate radial gradient
for y in range(img_height):
    for x in range(img_width):
        dx = x - center_x
        dy = y - center_y
        dist = math.hypot(dx, dy)
        # closer to center = lower ratio = lighter
        ratio = dist / max_dist
        brightness_scale = 1 - ratio  # 1 at center, 0 at corners
        # apply brightness boost
        r = min(255, int(base_color[0] + center_lightness_boost * brightness_scale))
        g = min(255, int(base_color[1] + center_lightness_boost * brightness_scale))
        b = min(255, int(base_color[2] + center_lightness_boost * brightness_scale))
        img.putpixel((x, y), (r, g, b))

# prepare to draw text
draw = ImageDraw.Draw(img)

# ascii Art
ascii_art = pyfiglet.figlet_format(text)

# load font
font = ImageFont.truetype(r"C:\\Windows\\Fonts\\courbd.ttf", 24)
ascent, descent = font.getmetrics()
line_height = ascent + descent

# center the text
lines = ascii_art.split('\n')
total_text_height = line_height * len(lines)
y_text = (img_height - total_text_height) // 2

for line in lines:
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]
    x_text = (img_width - line_width) // 2
    draw.text((x_text, y_text), line, font=font, fill=(249, 249, 249))  # light text
    y_text += line_height

# save the final image
img.save("ascii_vertical_wallpaper.png")
