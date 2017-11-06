'''
Lab 10 - Unit Converter
Allow user to choose input unit and output unit
'''

dist = float(input("What is the distance? "))  # prompt for distance

unit_in = (input("What is the input unit (ft, mi, m, km, yd, in)? "))  # prompt for unit type
unit_in = unit_in.lower()

unit_out = (input("What is the output unit (ft, mi, m, km, yd, in)? "))  # prompt for unit type
unit_out = unit_out.lower()

if unit_in == "ft":  # if unit is feet
    dist_conv = dist * 0.3048  # apply conversion
if unit_in == "mi":  # if unit is miles
    dist_conv = dist * 1609.34  # apply conversion
if unit_in == "m":  # if unit is meters
    dist_conv = dist * 1  # apply conversion
if unit_in == "km":  # if unit is in kilometers
    dist_conv = dist * 1000  # apply conversion
if unit_in == "yd":  # if unit is in yards
    dist_conv = dist * 0.9144  # apply conversion
if unit_in == "in":  # if unit is in inches
    dist_conv = dist * 0.0254  # apply conversion

if unit_out == "ft":  # if unit is feet
    dist_out = dist_conv * 3.2808  # apply conversion
if unit_out == "mi":  # if unit is miles
    dist_out = dist_conv * 0.0006  # apply conversion
if unit_out == "m":  # if unit is meters
    dist_out = dist_conv * 1  # apply conversion
if unit_out == "km":  # if unit is in kilometers
    dist_out = dist_conv * 0.001  # apply conversion
if unit_out == "yd":  # if unit is in yards
    dist_out = dist_conv * 1.935  # apply conversion
if unit_out == "in":  # if unit is in inches
    dist_out = dist_conv * 39.3700  # apply conversion

print(str(dist) + str(unit_in) + " is " + str(round(dist_out, 4)) + unit_out)  # output distance
