import numpy as np
from pgm import PGM
from statistics import mean
from scipy.ndimage import prewitt, sobel, laplace

# Prewitt mask
def prewitt_mask(image):
    np_pixels = np.array(image.pixels)
    np_pixels = np_pixels.astype(int)
    image.pixels = np.clip(prewitt(np_pixels), 0, 255)
    image.save("_Prewitt_mask")

# Sobel mask
def sobel_mask(image):
    np_pixels = np.array(image.pixels)
    np_pixels = np_pixels.astype(int)
    image.pixels = np.clip(sobel(np_pixels), 0, 255)
    image.save("_Sobel_mask")

# Laplacian mask
def laplace_mask(image):
    np_pixels = np.array(image.pixels)
    np_pixels = np_pixels.astype(int)
    image.pixels = np.clip(laplace(np_pixels), 0, 255)
    print(image.pixels)
    image.save("_Laplacian_mask")

pgm = PGM("lenna")
prewitt_mask(pgm)
sobel_mask(pgm)
laplace_mask(pgm)