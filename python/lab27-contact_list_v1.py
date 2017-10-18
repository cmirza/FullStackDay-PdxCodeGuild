'''
Lab 27 - Contact List
'''

contacts = []  # define contacts list

with open('contacts_v1.csv', 'r') as f:  # open contacts csv
    f.readline()  # skip header line
    for line in f:  # loop through each line of csv
        line = line.strip('\n')  # remove newline
        line = line.strip('"')  # strip quotes
        name, fav_fruit, fav_color = line.split(',')  # split on comma and assign to vars
        new_dict = {'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color}  # create dictionary
        contacts.append(dict(new_dict))  # add dictionary to list
    f.close()  # close file

print(contacts)  # print the contacts list
