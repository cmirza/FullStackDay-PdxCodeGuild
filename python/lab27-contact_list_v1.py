'''
Lab 27 - Contact List
'''

contacts = []

with open('contacts.csv', 'r') as f:
    f.readline()  # skip first line
    for line in f:
        line = line.strip('\n')  # remove newline
        line = line.strip('"')  # strip quotes
        name, fav_fruit, fav_color = line.split(',')  # split on comma and assign to vars
        new_dict = {'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color}  # create dictionary
        contacts.append(dict(new_dict))  # add dictionary to list

print(contacts)
