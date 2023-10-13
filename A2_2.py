import numpy as np
from pgm import PGM
from statistics import mean

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
                flat_array = get_section(np_pixels, [x,y], offset).astype(int).flatten()
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
        temp_pixels = np.zeros((image.x,image.y))
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


average(PGM("lenna"), 7)
average(PGM("lenna"), 15)

gaussian(PGM("lenna"), 7)
gaussian(PGM("lenna"), 15)

average(PGM("sf"), 7)
average(PGM("sf"), 15)

gaussian(PGM("sf"), 7)
gaussian(PGM("sf"), 15)