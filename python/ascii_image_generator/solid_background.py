from PIL import Image, ImageDraw, ImageFont  # Python Image Library for image manipulation
import pyfiglet  # generates ASCII art from plain text

# create ASCII art from text
ascii_art = pyfiglet.figlet_format("Melanie")

# final image size and background color
img_width = 1080
img_height = 1920
img_color = (24, 62, 125)

# generate a blank image with the specified size and color
img = Image.new("RGB", (img_width, img_height), color=img_color)
draw = ImageDraw.Draw(img)

# load font and size
font = ImageFont.truetype(r"C:\\Windows\\Fonts\\courbd.ttf", 24)

# get font character height in pixels: ascent is above baseline, descent is below baseline
ascent, descent = font.getmetrics()
# total line height is sum of ascent and descent, used to space each line of ASCII art correctly
line_height = ascent + descent

# split ASCII art into individual lines by breaking at newline characters
lines = ascii_art.split('\n')
# calculate total height of all lines combined to know how tall the whole ASCII block is
total_text_height = line_height * len(lines)
# calculate starting y-position to vertically center ASCII art in the image
y_text = (img_height - total_text_height) // 2

# loop through each line of the ASCII art
for line in lines:
    # calculate the width of the current line using font bounding box (right - left)
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]
    # calculate x position to horizontally center the line within the image
    x_text = (img_width - line_width) // 2
    # draw the text line at calculated (x, y) position with the chosen font and color
    draw.text((x_text, y_text), line, font=font, fill=(249, 249, 249))
    # move the y position down by one line height to prepare for next line
    y_text += line_height

# save image as
img.save("ascii_vertical_wallpaper.png")
