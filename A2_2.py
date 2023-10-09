import numpy as np
from pgm import PGM
from statistics import mean

# Average filter
def average(image, size):
    if size % 2 == 0:
        print("Error: size must be an odd integer")
        return
    else:
        offset = int(-(size - 1) / 2)
        np_pixels = np.array(image.pixels)
        temp_pixels = np.empty_like(np_pixels)
        for x in range(len(image.pixels)):
            for y in range(len(image.pixels[x])):
                flat_array = np_pixels[np.clip(x+offset, 0, 255) : np.clip(x+size, 0, 255), np.clip(y+offset, 0, 255) : np.clip(y+size, 0, 255)].astype(int).flatten()
                # print(str(np.clip(x+offset, 0, 255)) + " " + str(np.clip(x+size, 0, 255)))
                # print(str(np.clip(y+offset, 0, 255)) + " " + str(np.clip(y+size, 0, 255)))
                temp_pixels[x][y] = mean(flat_array)
        print(temp_pixels)
        print(type(temp_pixels))
        image.pixels = temp_pixels
        image.save("_avg" + "_" + str(size))


pgm = PGM("lenna")
average(pgm, 7)
average(pgm, 15)