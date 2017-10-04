'''
Lab 10 - Unit Converter
'''

dist = float(input("What is the distance in feet? "))  # prompt for distance in feet

dist_m = dist * 0.3048  # convert feet into meters, assign to new var

print(str(int(dist)) + "ft is " + str(round(dist_m, 4)) + "m")  # output distance in feet and distance in meters
