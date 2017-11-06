'''
Lab 10 - Unit Converter
Allow user to to choose type of unit, add yards and inches
'''

dist = float(input("What is the distance? "))  # prompt for distance

unit = (input("What is the unit (ft, mi, m, km, yd, in)? "))  # prompt for unit type
unit = unit.lower()

if unit == "ft":  # if unit is feet
    dist_m = dist * 0.3048  # apply conversion
    print(str(dist) + str(unit) + " is " + str(round(dist_m, 4)) + "m")  # output distance in meters

if unit == "mi":  # if unit is miles
    dist_m = dist * 1609.34  # apply conversion
    print(str(dist) + str(unit) + " is " + str(round(dist_m, 4)) + "m")  # output distance in meters

if unit == "m":  # if unit is meters
    dist_m = dist * 1  # apply conversion
    print(str(dist) + str(unit) + " is " + str(round(dist_m, 4)) + "m")  # output distance in meters

if unit == "km":  # if unit is in kilometers
    dist_m = dist * 1000  # apply conversion
    print(str(dist) + str(unit) + " is " + str(round(dist_m, 4)) + "m")  # output distance in meters

if unit == "yd":  # if unit is in yards
    dist_m = dist * 0.9144  # apply conversion
    print(str(dist) + str(unit) + " is " + str(round(dist_m, 4)) + "m")  # output distance in meters

if unit == "in":  # if unit is in inches
    dist_m = dist * 0.0254  # apply conversion
    print(str(dist) + str(unit) + " is " + str(round(dist_m, 4)) + "m")  # output distance in meters