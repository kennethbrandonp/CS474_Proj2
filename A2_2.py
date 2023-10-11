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
        # Set radius and sigma
        offset = int((size - 1) / 2)
        sigma = (float(size) / 5.0)
        # Create guassian mask with a sum of 1.0
        gauss_matrix = gaussian_matrix(size, sigma)
        np_pixels = np.array(image.pixels)
        temp_pixels = np.zeros((256,256))
        for x in range(len(image.pixels)):
            for y in range(len(image.pixels[x])):
                temp_array = get_section(np_pixels, [x,y], offset)
                temp_pixels[x][y] = int(sum(sum(temp_array.astype(float) * gauss_matrix)))
        image.pixels = temp_pixels.astype(int)
        image.save("_gaussian" + "_" + str(size))

# Create gaussian mask with a sum of 1.0
def gaussian_matrix(size, sigma):
    axis = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    gauss = np.exp(-0.5 * np.square(axis) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

# Get section of array and pad edge values
def get_section(arr, center, square_radius):
    tp = max(0, -(center[0] - square_radius))
    bp = max(0, -((arr.shape[0]-center[0]-1) - square_radius))
    lp = max(0, -(center[1] - square_radius))
    rp = max(0, -((arr.shape[1]-center[1]-1) - square_radius))
    arr = np.pad(arr, [[tp, bp], [lp, rp]], 'edge')
    return arr[center[0] - square_radius + tp:center[0] + square_radius + 1 + tp, \
              center[1] - square_radius + lp:center[1] + square_radius + 1 + lp]


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