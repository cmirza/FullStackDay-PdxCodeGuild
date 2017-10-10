'''
Lab 18 - Image Manipulation
Use the Pillow library to draw a stick figure.
'''

from PIL import Image, ImageDraw # import Image and ImageDraw library from Pillow

# set canvas size to 500 x 500 pixels
width = 500
height = 500

img = Image.new('RGB', (width, height))  # set img as new image

draw = ImageDraw.Draw(img)  # define draw variable

# draw white rectangle for background

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw pink lines for arms and legs
color = (256, 128, 128)  # pink
draw.line((250, 200, 340, 200), fill=color)  # arm 1
draw.line((250, 200, 160, 200), fill=color)  # arm 2
draw.line((250, 250, 340, 425), fill=color)  # leg 1
draw.line((250, 250, 160, 425), fill=color)  # leg 2

# draw a green circle for head
circle_x = width/2
circle_y = 100
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

# draw blue rectangle for torso
draw.rectangle(((200, 150), (300, 350)), fill="lightblue")

img.show()  # display image
