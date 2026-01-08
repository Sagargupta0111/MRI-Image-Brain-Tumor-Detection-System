"""
Create a professional MRI brain imaging background image
for the web application
"""

from PIL import Image, ImageDraw, ImageFilter
import os

# Create output directory
os.makedirs('static', exist_ok=True)

# Create a professional MRI-themed background
width, height = 1920, 1080

# Create base image with gradient-like effect
img = Image.new('RGB', (width, height), color=(15, 32, 48))

# Add some visual elements to make it look like MRI/medical theme
draw = ImageDraw.Draw(img, 'RGBA')

# Add subtle grid/pattern
for x in range(0, width, 100):
    draw.line([(x, 0), (x, height)], fill=(30, 60, 100, 20), width=1)

for y in range(0, height, 100):
    draw.line([(0, y), (width, y)], fill=(30, 60, 100, 20), width=1)

# Add some brain-like circular elements (subtle)
colors = [
    (100, 150, 200, 60),
    (80, 130, 180, 50),
    (60, 110, 160, 40),
]

# Add circles to simulate brain imaging
import math
for i in range(5):
    for j in range(3):
        x = int(width * (i + 1) / 6 + math.sin(i) * 100)
        y = int(height * (j + 1) / 4 + math.cos(j) * 80)
        r = 150 - i * 30
        draw.ellipse([x-r, y-r, x+r, y+r], fill=colors[i % len(colors)])

# Add a medical/tech vibe with some glowing lines
for i in range(3):
    draw.line(
        [(0, int(height * (i+1) / 4)), (width, int(height * (i+1) / 4))],
        fill=(100, 180, 220, 30),
        width=3
    )

# Apply slight blur for modern look
img = img.filter(ImageFilter.GaussianBlur(radius=2))

# Save the image
output_path = os.path.join('static', 'brain_bg.png')
img.save(output_path)

print(f'✓ Background image created: {output_path}')
print(f'  Size: {width}x{height}')
print(f'  Theme: Medical/MRI styled')
