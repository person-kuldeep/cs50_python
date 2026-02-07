from PIL import Image, ImageDraw
import random

# Create a 3:2 ratio image (600x400 pixels)
width, height = 600, 400
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Generate random colors
bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
shape_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
accent_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Fill background
draw.rectangle([0, 0, width, height], fill=bg_color)

# Draw random shapes
center_x, center_y = width // 2, height // 2

# Draw circles
for i in range(random.randint(3, 6)):
    radius = random.randint(30, 120)
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=shape_color, outline=accent_color, width=2)

# Draw rectangles
for i in range(random.randint(2, 4)):
    x1 = random.randint(20, width - 100)
    y1 = random.randint(20, height - 100)
    x2 = x1 + random.randint(50, 150)
    y2 = y1 + random.randint(50, 150)
    draw.rectangle([x1, y1, x2, y2], fill=accent_color, outline=shape_color, width=2)

# Draw some lines
for i in range(random.randint(5, 10)):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    draw.line([x1, y1, x2, y2], fill=accent_color, width=random.randint(1, 3))

# Save the image
image.save('random_logo.png')
print("Random logo generated: random_logo.png (600x400, 3:2 ratio)")
