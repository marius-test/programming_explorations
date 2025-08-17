from PIL import Image, ImageDraw, ImageFont
import pyfiglet

# text and settings
text = "marius-x86"  # text to convert into ASCII art
img_width = 1080  # width of the output image in pixels
img_height = 1920  # height of the output image in pixels
img_color = (0, 0, 128)  # solid background color (teal)
font_path = r"C:\\Windows\\Fonts\\courbd.ttf"  # path to font file
font_size = 24  # font size for ASCII art rendering
text_color = (249, 249, 249)  # light text color (near white)

# generate ASCII art from the text string
ascii_art = pyfiglet.figlet_format(text)

# create a new solid background image with given color and size
img = Image.new("RGB", (img_width, img_height), color=img_color)
draw = ImageDraw.Draw(img)  # create drawing context for the image

# load the font with the specified size
font = ImageFont.truetype(font_path, font_size)
ascent, descent = font.getmetrics()  # get font metrics for vertical spacing
line_height = ascent + descent  # total line height including descent

# split the ASCII art text into individual lines
lines = ascii_art.split("\n")
# calculate total height of all lines combined to center vertically
total_text_height = line_height * len(lines)
y_text = (img_height - total_text_height) // 2  # starting y position (vertical center)

# draw each line of ASCII art with a heavier bold effect by drawing multiple offsets
for line in lines:
    if not line.strip():
        # if line is empty, just move down by line height
        y_text += line_height
        continue
    
    # get width of the current line in pixels
    line_width = font.getbbox(line)[2] - font.getbbox(line)[0]
    # calculate x position to horizontally center the line
    x_text = (img_width - line_width) // 2
    
    # offsets for heavier bold effect (draw text multiple times around base position)
    offsets = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1)]
    
    # draw the text at each offset to simulate boldness
    for ox, oy in offsets:
        draw.text((x_text + ox, y_text + oy), line, font=font, fill=text_color)
    
    # move y position down by one line height for next line
    y_text += line_height

# save the final image to disk
img.save(r"C:\\Users\\marius\\python\\programming_explorations\\python\\ascii_image_generator\\images\\ascii_vertical_wallpaper_13.png")
