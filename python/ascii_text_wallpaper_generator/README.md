# ascii_text_wallpaper_generator

A lightweight Python project to generate ASCII text wallpapers with solid or smooth radial gradient backgrounds.

### Features

- Convert any text into ASCII text using **pyfiglet**.
- Generate solid color backgrounds or smooth radial gradient/vignette backgrounds.
- Save wallpapers as images (PNG).
- Supports custom font and size for ASCII text.

### Installation

1. Clone the repository:  
   ```bash
   git clone <repo-url>
   ```
2. Install dependencies:  
   ```bash
   pip install pyfiglet pillow numpy
   ```

### Scripts

- `ascii_test.py`          : Quick test, prints ASCII text in the console.  
- `solid_background.py`    : Generates wallpapers with a solid background.  
- `gradient_background.py` : Generates wallpapers with a smooth radial gradient background.  

### Usage

1. Edit the `text` variable in any script to change the ASCII text.  
2. Adjust parameters as needed:  
   - `img_width`, `img_height` → size of the wallpaper in pixels.  
   - `font_path`, `font_size` → font file and size for ASCII text.  
   - `base_color` → RGB color of the background.  
   - `min_brightness` → controls vignette brightness at edges (0 = dark edges, 1 = no vignette).  
3. Run the script:  
   ```bash
   python gradient_background.py
   ```
4. Generated wallpapers are saved in the `images/` folder.

### Tips

- The gradient uses a smooth radial falloff for a professional look.  
- You can tweak the smoothness by modifying the formula in `gradient_background.py`. For example:

**Quadratic smooth falloff:**  
```python
brightness_scale = min_brightness + (1 - min_brightness) * (1 - ratio) ** 2
```

**Cosine-based smooth falloff:**  
```python
brightness_scale = min_brightness + (1 - min_brightness) * np.cos(ratio * (pi / 2))
```

### Folder Structure

```text
ascii_text_wallpaper_generator/
├── images/                  # generated wallpapers
├── ascii_text_test.py
├── solid_background.py
├── gradient_background.py
└── README.md
```

### License

MIT License
