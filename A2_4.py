import numpy as np
from pgm import PGM
from statistics import mean

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
        return temp_pixels

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

# Unsharp mask
def high_boost(image, k):
    offset = 3
    size = 7
    np_pixels = np.array(image.pixels).astype(float)
    lp_pixels = gaussian(image, size).astype(float)
    mask = np_pixels - lp_pixels
    np_pixels += (k * mask)
    # Clip values from 0 to 255
    np_pixels = np.clip(np_pixels, 0, (image.quantization - 1))
    image.pixels = np_pixels.astype(int)
    image.save("_boost" + "_k" + str(k))

high_boost(PGM("lenna"), 1)
high_boost(PGM("lenna"), 2)
high_boost(PGM("lenna"), 3)

high_boost(PGM("f_16"), 1)
high_boost(PGM("f_16"), 2)
high_boost(PGM("f_16"), 3)

# Note: Lenna looks best with k=1, f_16 looks best with k=2