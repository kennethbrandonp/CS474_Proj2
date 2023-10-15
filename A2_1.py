from pgm import PGM, np

def correlation(pgm, size, weights):
    padding = size // 2 #Equal padding
    for x in range(padding, pgm.x - padding):
        for y in range(padding, pgm.y - padding):
            #Filtered pixel value to store:
            filteredPixel = 0

            #Apply filter to window of pixels:
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    #Apply filter weights to pixels:
                    pixel_value = pgm.pixels[x + i][y + j]
                    weight = weights[(i + padding) * size + (j + padding)]
                    filteredPixel += pixel_value * weight #Dot product
            if filteredPixel > 255:
                filteredPixel = 255 #Rescaling
            #Store the filtered pixel value in the filtered image:
            pgm.pixels[x][y] = int(filteredPixel)

    pgm.save("corResult")  #Save result

def extractSizeAndWeights(pgm):
    #Grab the image size by picking the smallest of the two dimensions:
    size = min(pgm.x, pgm.y)
    
    weights = []    #Container for the weights of pattern.pgm
    padding = (pgm.x - size) // 2   #Equal padding to each side of the weights, truncates so we don't use decimal values
    for i in range(padding, padding + size):
        if i < 0 or i >= pgm.x:
            continue  #Out of bound skip
        for j in range(padding, padding + size):
            if j < 0 or j >= pgm.y:
                continue  #Out of bound skip
            weights.append(pgm.pixels[i][j])

    return size, weights


#Spatial filtering (Correlation) using two instances of PGM
image = PGM("image")
pattern = PGM("pattern") 
size, weights = extractSizeAndWeights(pattern)
correlation(image, 3, weights)  #Apply the filter