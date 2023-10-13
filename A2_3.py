from pgm import PGM, np, random
from A2_2 import average

def medianFilter(pgm, size):
        for i in range(pgm.x):
            for j in range(pgm.y):
                #If the current pixel is near the border of the image
                if i < size // 2 or j < size // 2 or i >= pgm.x - size // 2 or j >= pgm.y - size // 2:
                    #This skips border pixels
                    continue
                
                #Empty window for pixel values
                window = []
                #Loop through rows
                for x in range(i - size // 2, i + size // 2 + 1):
                #Loop through columns
                    for y in range(j - size // 2, j + size // 2 + 1):
                    #Place current pixel value in filter window
                        window.append(pgm.pixels[x][y])
                        
                #Set current pixel to median value
                window.sort()
                median = len(window) // 2
                pgm.pixels[i][j] = window[median]

def applyNoise(pgm, noiseFactor):  #Salt and pepper noise
    for i in range(pgm.x):
        for j in range(pgm.y):
            #Set pixel to black: (pepper)
            if random.random() < noiseFactor / 200:
                pgm.pixels[i][j] = 0 
                #Set pixel to white: (salt)
            elif random.random() < noiseFactor / 100:
                pgm.pixels[i][j] = 255  
            
#For the photo lenna:
#Noise 30, size 7x7
image = PGM("lenna")
comparisonImage = PGM("lenna")  #For averaging
applyNoise(image, 30)
applyNoise(comparisonImage, 30)
image.save("noise30")
medianFilter(image, 7)
average(comparisonImage, 7)
image.save("30median7x7")
comparisonImage.save("30average7x7")

#Noise 30, size 15x15
image = PGM("lenna")
comparisonImage = PGM("lenna")  #For averaging
applyNoise(image, 30)
applyNoise(comparisonImage, 30)
medianFilter(image, 15)
average(comparisonImage, 15)
image.save("30median15x15")
comparisonImage.save("30average15x15")

#Noise 50, size 7x7
image = PGM("lenna")
comparisonImage = PGM("lenna")  #For averaging
applyNoise(image, 50)
applyNoise(comparisonImage, 50)
image.save("noise50")
medianFilter(image, 7)
average(comparisonImage, 7)
image.save("50median7x7")
comparisonImage.save("50average7x7")

#Noise 50, size 15x15
image = PGM("lenna")
comparisonImage = PGM("lenna")  #For averaging
applyNoise(image, 50)
applyNoise(comparisonImage, 50)
medianFilter(image, 15)
average(comparisonImage, 15)
image.save("50median15x15")
comparisonImage.save("50average15x15")

#For the photo boat:
#Noise 30, size 7x7
image = PGM("boat")
comparisonImage = PGM("boat")  #For averaging
applyNoise(image, 30)
applyNoise(comparisonImage, 30)
image.save("noise30")
medianFilter(image, 7)
average(comparisonImage, 7)
image.save("30median7x7")
comparisonImage.save("30average7x7")

#Noise 30, size 15x15
image = PGM("boat")
comparisonImage = PGM("boat")  #For averaging
applyNoise(image, 30)
applyNoise(comparisonImage, 30)
medianFilter(image, 15)
average(comparisonImage, 15)
image.save("30median15x15")
comparisonImage.save("30average15x15")

#Noise 50, size 7x7
image = PGM("boat")
comparisonImage = PGM("boat")  #For averaging
applyNoise(image, 50)
applyNoise(comparisonImage, 50)
image.save("noise50")
medianFilter(image, 7)
average(comparisonImage, 7)
image.save("50median7x7")
comparisonImage.save("50average7x7")

#Noise 50, size 15x15
image = PGM("boat")
comparisonImage = PGM("boat")  #For averaging
applyNoise(image, 50)
applyNoise(comparisonImage, 50)
medianFilter(image, 15)
average(comparisonImage, 15)
image.save("50median15x15")
comparisonImage.save("50average15x15")