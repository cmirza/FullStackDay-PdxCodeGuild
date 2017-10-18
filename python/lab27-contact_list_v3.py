'''
Lab 27 - Contact List
'''

contacts = []

with open('contacts.csv', 'r+') as f:
    f.readline()  # skip first line
    for line in f:
        line = line.strip('\n')  # remove newline
        line = line.strip('"')  # strip quotes
        name, fav_fruit, fav_color = line.split(',')  # split on comma and assign to vars
        new_dict = {'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color}  # create dictionary
        contacts.append(dict(new_dict))  # add dictionary to list


def create_repl():
    c_name = input('Enter a name: ')
    c_fav_fruit = input('Enter favorite fruit: ')
    c_fav_color = input('Enter favorite color: ')
    c_new_dict = {'name': c_name, 'favorite fruit': c_fav_fruit, 'favorite color': c_fav_color}
    contacts.append(dict(c_new_dict))
    return 'Done.'


def read_repl():
    input_name = input('Enter a name to search for: ')
    for item in contacts:
        if item['name'] == input_name:
            return item
    else:
        return 'Not found.'


def update_repl():
    input_name = input('Enter a name to update: ')
    for item in contacts:
        if item['name'] == input_name:
            u_fav_fruit = input('Enter updated fruit: ')
            u_fav_color = input('Enter updated color: ')
            item['favorite fruit'] = u_fav_fruit
            item['favorite color'] = u_fav_color
            return 'Done.'
    else:
        return 'Not found.'


def delete_repl():
    input_name = input('Enter a name to delete: ')
    for item in contacts:
        if item['name'] == input_name:
            contacts.remove(item)
            return 'Done.'
    else:
        return 'Not found.'


while True:
    u_input = input('Would you like to (c)reate, (r)ead, (u)pdate or (d)elete a record: ')
    if u_input == 'c':
        print(create_repl())
    elif u_input == 'r':
        print(read_repl())
    elif u_input == 'u':
        print(update_repl())
    elif u_input == 'd':
        print(delete_repl())
    elif u_input == 'exit':
        with open('contacts.csv', 'w+') as f:
            f.write('Name,Favorite Fruit,Favorite Color\n')
            for item in contacts:
                f.write(item['name']+','+item['favorite fruit']+','+item['favorite color']+'\n')
        break
    else:
        print('Invalid input.')
