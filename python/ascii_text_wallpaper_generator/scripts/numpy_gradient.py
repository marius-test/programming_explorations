import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pyfiglet
import math

# settings
text = "marius-x86"  # text to convert into ASCII art
img_width = 1080  # width of the final image in pixels
img_height = 1920  # height of the final image in pixels
base_color = np.array([0, 128, 128], dtype=np.float32)  # teal base color as RGB float array

# brightness settings for vignette effect
min_brightness = 0.8  # minimum brightness at edges (closer to 1 means brighter middle)

# create coordinate grids for all pixels
y_indices, x_indices = np.indices((img_height, img_width))
center_x = img_width // 2  # horizontal center of image
center_y = img_height // 2  # vertical center of image

# calculate distance from each pixel to center using Euclidean distance
dx = x_indices - center_x  # horizontal distance from center
dy = y_indices - center_y  # vertical distance from center
distances = np.hypot(dx, dy)  # Euclidean distance for each pixel

# normalize distances to range 0 (center) to 1 (farthest corner)
max_dist = math.hypot(center_x, center_y)  # max distance (corner to center)
ratio = distances / max_dist  # normalize distances

# calculate brightness scale with sharper falloff near edges (power 6)
brightness_scale = min_brightness + (1 - min_brightness) * (1 - ratio) ** 8

# apply brightness scale to base color channels (broadcast to RGB)
gradient = (base_color * brightness_scale[..., None]).astype(np.uint8)

# create PIL image from the numpy array gradient
img = Image.fromarray(gradient, mode="RGB")

# prepare to draw text on the image
draw = ImageDraw.Draw(img)
ascii_art = pyfiglet.figlet_format(text)  # generate ASCII art from text

# load font and get font metrics for line height calculation
font = ImageFont.truetype(r"C:\\Windows\\Fonts\\courbd.ttf", 24)
ascent, descent = font.getmetrics()  # ascent is height above baseline, descent below
line_height = ascent + descent  # total line height including descent
lines = ascii_art.split('\n')  # split ascii art into lines
total_text_height = line_height * len(lines)  # total height of all lines combined
y_text = (img_height - total_text_height) // 2  # vertical start pos to center text

# draw each ASCII art line with a bold effect (4 offsets)
for line in lines:
    if not line.strip():
        y_text += line_height  # skip empty lines, move y down
        continue
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]  # width of line in pixels
    x_text = (img_width - line_width) // 2  # horizontal center position for the line
    
    # draw text multiple times with slight offsets to simulate bold
    offsets = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for ox, oy in offsets:
        draw.text((x_text + ox, y_text + oy), line, font=font, fill=(249, 249, 249))
    y_text += line_height  # move y down to next line

# save the final image to disk
img.save(r"C:\\Users\\marius\\python\\programming_explorations\\python\\ascii_image_generator\\images\\ascii_vertical_wallpaper_11.png")
