import numpy as np
from pgm import PGM
from statistics import mean
from scipy.ndimage import gaussian_filter

# Average filter
def average(image, size):
    if size % 2 == 0:
        print("Error: size must be an odd integer")
        return
    else:
        offset = int((size - 1) / 2)
        np_pixels = np.array(image.pixels)
        temp_pixels = np.empty_like(np_pixels)
        for x in range(len(image.pixels)):
            for y in range(len(image.pixels[x])):
                flat_array = np_pixels[np.clip(x-offset, 0, 255) : np.clip(x+offset+1, 0, 255), np.clip(y-offset, 0, 255) : np.clip(y+offset+1, 0, 255)].astype(int).flatten()
                temp_pixels[x][y] = mean(flat_array)
        image.pixels = temp_pixels
        image.save("_avg" + "_" + str(size))

# Gaussian filter
def gaussian(image, size):
    if size % 2 == 0:
        print("Error: size must be an odd integer")
        return
    else:
        offset = int((size - 1) / 2)
        np_pixels = np.array(image.pixels)
        temp_pixels = (gaussian_filter(np_pixels.astype(int), sigma=(float(size)/5.0), radius=offset))
        image.pixels = temp_pixels
        image.save("_gaussian" + "_" + str(size))

pgm = PGM("lenna")
average(pgm, 7)
average(pgm, 15)
gaussian(pgm, 7)
gaussian(pgm, 15)
pgm = PGM("sf")
average(pgm, 7)
average(pgm, 15)
gaussian(pgm, 7)
gaussian(pgm, 15)
