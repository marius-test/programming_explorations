from PIL import Image, ImageDraw, ImageFont  # Python Image Library for image manipulation
import pyfiglet  # generates ASCII art from plain text
import math  # math functions, used for distance calculations

# settings
text = "Melanie"  # text to convert into ASCII art
img_width = 1080  # image width in pixels
img_height = 1920  # image height in pixels
base_color = (24, 62, 125)  # dark blue base color for background
center_lightness_boost = 100  # how much lighter the center will be compared to edges

# create a blank RGB image without background color set yet
img = Image.new("RGB", (img_width, img_height))

# find the center coordinates of the image
center_x = img_width // 2
center_y = img_height // 2

# maximum distance from center to any corner (used for gradient scaling)
max_dist = math.hypot(center_x, center_y)

# generate radial gradient background by adjusting brightness based on distance from center
for y in range(img_height):
    for x in range(img_width):
        dx = x - center_x  # horizontal distance from center
        dy = y - center_y  # vertical distance from center
        dist = math.hypot(dx, dy)  # actual distance from center using Pythagoras
        ratio = dist / max_dist  # normalize distance: 0 at center, 1 at farthest corner
        brightness_scale = 1 - ratio  # invert ratio so center is brightest (1), edges darkest (0)
        
        # calculate new RGB values by adding brightness boost scaled by distance
        r = min(255, int(base_color[0] + center_lightness_boost * brightness_scale))
        g = min(255, int(base_color[1] + center_lightness_boost * brightness_scale))
        b = min(255, int(base_color[2] + center_lightness_boost * brightness_scale))
        
        # set pixel color to the calculated gradient color
        img.putpixel((x, y), (r, g, b))

# prepare to draw ASCII text on the image
draw = ImageDraw.Draw(img)

# generate ASCII art from the given text
ascii_art = pyfiglet.figlet_format(text)

# load font to be used for drawing text
font = ImageFont.truetype(r"C:\\Windows\\Fonts\\courbd.ttf", 24)

# get font metrics for line height calculations
ascent, descent = font.getmetrics()
line_height = ascent + descent

# split ASCII art into lines and calculate total height of all lines combined
lines = ascii_art.split('\n')
total_text_height = line_height * len(lines)

# starting y position to vertically center ASCII art in the image
y_text = (img_height - total_text_height) // 2

# loop through each ASCII art line and draw it centered horizontally
for line in lines:
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]  # calculate line width
    x_text = (img_width - line_width) // 2  # calculate x position to center text line
    draw.text((x_text, y_text), line, font=font, fill=(249, 249, 249))  # draw text in light color
    y_text += line_height  # move y position down for next line

# save the final image to file
img.save("ascii_vertical_wallpaper_2.png")
