import numpy as np
from pgm import PGM
from statistics import mean
from scipy.ndimage import gaussian_filter

# Unsharp mask
def high_boost(image, k):
    offset = 3
    size = 7
    np_pixels = np.array(image.pixels)
    np_pixels = np_pixels.astype(int)
    lp_pixels = (gaussian_filter(np_pixels, sigma=(float(size)/5.0), radius=offset))
    mask = np_pixels - lp_pixels
    image.pixels = np.clip((np_pixels + (k * mask).astype(int)), 0, 255)
    image.save("_boost" + "_k" + str(k))

pgm = PGM("lenna")
high_boost(pgm, 1.0)
high_boost(pgm, 1.5)
high_boost(pgm, 2.0)

pgm = PGM("f_16")
high_boost(pgm, 1.0)
high_boost(pgm, 1.5)
high_boost(pgm, 2.0)

# Note: lenna looks best with k=1.0, f_16 looks best with k=1.5
