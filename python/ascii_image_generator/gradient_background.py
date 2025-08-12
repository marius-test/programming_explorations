from PIL import Image, ImageDraw, ImageFont  # Python Image Library for image manipulation
import pyfiglet  # generates ASCII art from plain text
import math  # math functions, used for distance calculations

# settings
text = "marius-x86"  # text to convert into ASCII art
img_width = 2560  # image width in pixels
img_height = 1440  # image height in pixels
base_color = (0, 128, 128)  # dark blue base color for background

# create a blank RGB image without background color set yet
img = Image.new("RGB", (img_width, img_height))

# find the center coordinates of the image
center_x = img_width // 2
center_y = img_height // 2

# maximum distance from center to any corner (used for gradient scaling)
max_dist = math.hypot(center_x, center_y)

# vignette settings
min_brightness = 0.7  # how dark the edges get (0 = black, 1 = no darkening)

# generate radial gradient background with center as base_color and edges darker (vignette)
for y in range(img_height):
    for x in range(img_width):
        dx = x - center_x  # horizontal distance from center
        dy = y - center_y  # vertical distance from center
        dist = math.hypot(dx, dy)  # actual distance from center using Pythagoras
        ratio = dist / max_dist  # normalize distance: 0 at center, 1 at farthest corner
        
        # calculate brightness scale for vignette effect
        brightness_scale = min_brightness + (1 - min_brightness) * (1 - ratio) ** 2
        
        # apply brightness scale to base color channels to darken edges
        r = int(base_color[0] * brightness_scale)
        g = int(base_color[1] * brightness_scale)
        b = int(base_color[2] * brightness_scale)
        
        # set pixel color to the calculated vignette color
        img.putpixel((x, y), (r, g, b))

# prepare to draw ASCII text on the image
draw = ImageDraw.Draw(img)

# generate ASCII art from the given text
ascii_art = pyfiglet.figlet_format(text)

# load font to be used for drawing text
font = ImageFont.truetype(r"C:\\Windows\\Fonts\\courbd.ttf", 36)

# get font metrics for line height calculations
ascent, descent = font.getmetrics()
line_height = ascent + descent

# split ASCII art into lines and calculate total height of all lines combined
lines = ascii_art.split('\n')
total_text_height = line_height * len(lines)

# starting y position to vertically center ASCII art in the image
y_text = (img_height - total_text_height) // 2

# loop through each ASCII art line and draw it centered horizontally with bold effect
for line in lines:
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]  # calculate line width
    x_text = (img_width - line_width) // 2  # calculate x position to center text line
    
    # draw text multiple times with slight offsets to simulate bold
    offsets = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for ox, oy in offsets:
        draw.text((x_text + ox, y_text + oy), line, font=font, fill=(249, 249, 249))
    
    y_text += line_height  # move y position down for next line

# save image as
img.save(r"C:\\Users\\marius\\python\\programming_explorations\\python\\ascii_image_generator\\images\\ascii_vertical_wallpaper_5.png")
