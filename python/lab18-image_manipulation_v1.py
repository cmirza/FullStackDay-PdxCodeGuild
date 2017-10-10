'''
Lab 18 - Image Manipulation
'''

from PIL import Image  # import Image library from Pillow
img = Image.open("lenna.png")  # open image
width, height = img.size  # extract width and height dimensions, assign them to list width and height
pixels = img.load()  # create pixel map

for i in range(width):  # run through the width
    for j in range(height):  # run through pixels in height
        r, g, b = pixels[i, j]  # for pixel (i, j), find RGB values

        y = 0.299 * r + 0.587 * g + 0.114 * b  # convert RGB values to greyscale
        r = int(y)  # convert float to int
        g = int(y)  # convert float to int
        b = int(y)  # convert float to int

        pixels[i, j] = (r, g, b)  # assign new greyscale values back to pixel

img.show()  # show modified image
