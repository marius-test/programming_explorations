# ascii_text_wallpaper_generator

A lightweight Python project to generate ASCII text wallpapers with solid or gradient backgrounds.  

### Features  

- Convert any text into ASCII text using pyfiglet.  
- Generate solid color backgrounds or gradient/vignette backgrounds.  
- Save wallpapers as images (PNG).  
- Supports custom font and size for ASCII text.  

### Installation  

1. Clone the repository:  
   git clone `<repo-url>`  
2. Install dependencies:  
   pip install pyfiglet pillow numpy  

### Scripts  

- ascii_test.py          : Quick test, prints ASCII text in the console.  
- solid_background.py    : Generates wallpapers with a solid background.  
- gradient_background.py : Generates wallpapers with a radial gradient background (less efficient).  
- numpy_gradient.py      : Faster gradient wallpaper generation using NumPy.  

### Usage  

- Edit the `text` variable in any script to change the ASCII text.  
- Adjust img_width, img_height, font_path, font_size, and base_color as needed.  
- Run a script: python solid_background.py  
- Generated wallpapers are saved in the `images` folder.  

### Folder Structure  

ascii_image_generator/  

- images/  # generated wallpapers  
- ascii_test.py  
- solid_background.py  
- gradient_background.py  
- numpy_gradient.py  
- README.txt  
  
License:  
MIT License  
