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
        for x in range(len(image.pixels)):
            for y in range(len(image.pixels[x])):
                flat_array = np.array(image.pixels[np.clip(x+offset, 0, 255) : np.clip(x+size, 0, 255)][np.clip(y+offset, 0, 255) : np.clip(y+size, 0, 255)]).astype(int).flatten()
                # print(str(np.clip(x+offset, 0, 255)) + " " + str(np.clip(x+size, 0, 255)))
                # print(str(np.clip(y+offset, 0, 255)) + " " + str(np.clip(y+size, 0, 255)))
                # print(mean(flat_array))
                print(image.pixels[0:7][7:17])


pgm = PGM("lenna")
print(pgm.pixels[0:7][7])
#average(pgm, 7)
#pgm.save("_avg")