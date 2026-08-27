import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# Image dimensions
WIDTH = 1920
HEIGHT = 1080

# rng = np.random.default_rng(501622731)
rng = np.random.default_rng()

def simple_biased_color(rng):
    r = rng.random()
    g = rng.uniform(0.25, 0.75)
    b = rng.uniform(0.5, 1.0)
    return np.array([r, g, b])

def biased_color(rng, bias_prob=0.5, hue_range=(0.49, 0.64)):
    if rng.random() < bias_prob:
        h = rng.uniform(*hue_range)
    else:
        h = rng.random()
    s = rng.uniform(0.5, 1.0)
    v = rng.uniform(0.5, 1.0)
    return hsv_to_rgb([h, s, v])

# Corner colors are fixed
fixed_colors = [simple_biased_color(rng) for _ in range(4)]

# Create normalized coordinate grids
x = np.linspace(0, 1, WIDTH)
y = np.linspace(0, 1, HEIGHT)
X, Y = np.meshgrid(x, y)

# Bilinear interpolation
image = (
    (1 - X)[..., None] * (1 - Y)[..., None] * fixed_colors[0] +
    X[..., None] * (1 - Y)[..., None] * fixed_colors[1] +
    (1 - X)[..., None] * Y[..., None] * fixed_colors[2] +
    X[..., None] * Y[..., None] * fixed_colors[3]
)

# Display the image
plt.figure(figsize=(6, 6), dpi=100)
plt.imshow(image, origin="upper")
plt.axis("off")

# Save the image
output_file = "wallpaper.png"
plt.savefig(output_file, dpi=100, bbox_inches="tight", pad_inches=0)
plt.close()

print(f"Saved image as '{output_file}'")
