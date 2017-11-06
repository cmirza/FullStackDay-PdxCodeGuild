'''
Lab 18 - Image Manipulation
Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue.
'''

from PIL import Image  # import Image library from Pillow
import colorsys  # import colorsys library

img = Image.open("lenna.png")  # open image
width, height = img.size  # extract width and height dimensions, assign them to list width and height
pixels = img.load()  # create pixel map

for i in range(width):  # run through the width
    for j in range(height):  # run through pixels in height
        r, g, b = pixels[i, j]  # for pixel (i, j), find RGB values
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)  # convert RGB values to HSV

        h = h + .05  # manipulate hue
        s = s + .5  # manipulate saturation
        v = v + .5  # manipulate value

        r, g, b = colorsys.hsv_to_rgb(h, s, v)  # convert HSV back to RGB

        r = int(r * 255)  # convert float to int
        g = int(g * 255)  # convert float to int
        b = int(b * 255)  # convert float to int

        pixels[i, j] = (r, g, b)  # assign new values back to pixel

img.show()  # show modified image
