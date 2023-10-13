import numpy as np
from pgm import PGM
from statistics import mean
from scipy.ndimage import prewitt, sobel, laplace

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

# Prewitt mask
def prewitt_mask(image):
    # Create Prewitt matrices
    Gx = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
    Gy = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
    offset = 1
    # Allocate partial derivative arrays
    temp_pixels_x = np.zeros((image.x,image.y))
    temp_pixels_y = np.zeros((image.x,image.y))
    # Get pixels from image
    np_pixels = np.array(image.pixels).astype(int)
    # Iterate mask over entire image on both axes to generate partial derivatives
    for x in range(len(image.pixels)):
        for y in range(len(image.pixels[x])):
            temp_array = get_section(np_pixels, [x,y], offset)
            temp_pixels_x[x][y] = sum(sum(temp_array.astype(float) * Gx))
            temp_pixels_y[x][y] = sum(sum(temp_array.astype(float) * Gy))

    # Normalizing values from 0 to quantization max for X partial derivative
    temp_pixels_x -= np.min(temp_pixels_x)
    temp_pixels_x = ((temp_pixels_x / np.max(temp_pixels_x)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_x
    image.save("_Prewitt_mask_X")

    # Calculating Y partial derivative
    # Normalizing values from 0 to quantization max for Y partial derivative
    temp_pixels_y -= np.min(temp_pixels_y)
    temp_pixels_y = ((temp_pixels_y / np.max(temp_pixels_y)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_y
    image.save("_Prewitt_mask_Y")

    # Calculating gradient magnitude
    temp_pixels_xy = np.sqrt(np.power(temp_pixels_x, 2) + np.power(temp_pixels_y, 2))
    # Normalizing values from 0 to quantization max
    temp_pixels_xy -= np.min(temp_pixels_xy)
    temp_pixels_xy = ((temp_pixels_xy / np.max(temp_pixels_xy)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_xy
    image.save("_Prewitt_mask_XY")

    # Sharpen image
    combined_pixels = np_pixels - temp_pixels_xy
    combined_pixels -= np.min(combined_pixels)
    combined_pixels = ((combined_pixels / np.max(combined_pixels)) * (image.quantization - 1)).astype(int)
    image.pixels = combined_pixels
    image.save("_Prewitt_sharp")

# Sobel mask
def sobel_mask(image):
    # Create Sobel matrices
    Gx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    Gy = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
    offset = 1
    # Allocate partial derivative arrays
    temp_pixels_x = np.zeros((image.x,image.y))
    temp_pixels_y = np.zeros((image.x,image.y))
    # Get pixels from image
    np_pixels = np.array(image.pixels).astype(int)
    # Iterate mask over entire image on both axes to generate partial derivatives
    for x in range(len(image.pixels)):
        for y in range(len(image.pixels[x])):
            temp_array = get_section(np_pixels, [x,y], offset)
            temp_pixels_x[x][y] = sum(sum(temp_array.astype(float) * Gx))
            temp_pixels_y[x][y] = sum(sum(temp_array.astype(float) * Gy))

    # Normalizing values from 0 to quantization max for X partial derivative
    temp_pixels_x -= np.min(temp_pixels_x)
    temp_pixels_x = ((temp_pixels_x / np.max(temp_pixels_x)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_x
    image.save("_Sobel_mask_X")

    # Calculating Y partial derivative
    # Normalizing values from 0 to quantization max for Y partial derivative
    temp_pixels_y -= np.min(temp_pixels_y)
    temp_pixels_y = ((temp_pixels_y / np.max(temp_pixels_y)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_y
    image.save("_Sobel_mask_Y")

    # Calculating gradient magnitude
    temp_pixels_xy = np.sqrt(np.power(temp_pixels_x, 2) + np.power(temp_pixels_y, 2))
    # Normalizing values from 0 to quantization max
    temp_pixels_xy -= np.min(temp_pixels_xy)
    temp_pixels_xy = ((temp_pixels_xy / np.max(temp_pixels_xy)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_xy
    image.save("_Sobel_mask_XY")

    # Sharpen image
    combined_pixels = np_pixels - temp_pixels_xy
    combined_pixels -= np.min(combined_pixels)
    combined_pixels = ((combined_pixels / np.max(combined_pixels)) * (image.quantization - 1)).astype(int)
    image.pixels = combined_pixels
    image.save("_Sobel_sharp")

# Laplacian mask
def laplace_mask(image):
    Gxy = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
    offset = 1
    # Allocate partial derivative array
    temp_pixels_xy = np.zeros((image.x,image.y))
    # Get pixels from image and apply weak gaussian filter to reduce noise
    np_pixels = gaussian(image, 5).astype(int)
    # Iterate mask over entire image on both axes to generate partial derivatives
    for x in range(len(image.pixels)):
        for y in range(len(image.pixels[x])):
            temp_array = get_section(np_pixels, [x,y], offset)
            temp_pixels_xy[x][y] = sum(sum(temp_array.astype(float) * Gxy))
    # Normalizing values from 0 to quantization max
    temp_pixels_xy -= np.min(temp_pixels_xy)
    temp_pixels_xy = ((temp_pixels_xy / np.max(temp_pixels_xy)) * (image.quantization - 1)).astype(int)
    # Combining filter and image to create sharpened image
    combined_pixels = image.pixels - temp_pixels_xy
    # Normalizing values from 0 to quantization max
    combined_pixels -= np.min(combined_pixels)
    combined_pixels = ((combined_pixels / np.max(combined_pixels)) * (image.quantization - 1)).astype(int)
    image.pixels = temp_pixels_xy
    image.save("_Laplacian_mask")
    image.pixels = combined_pixels
    image.save("_Laplacian_sharp")

prewitt_mask(PGM("lenna"))
prewitt_mask(PGM("sf"))

sobel_mask(PGM("lenna"))
sobel_mask(PGM("sf"))

laplace_mask(PGM("lenna"))
laplace_mask(PGM("sf"))