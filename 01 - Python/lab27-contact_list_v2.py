'''
Lab 27 - Contact List
Implement a CRUD REPL
'''

contacts = []  # define contacts list

# Open contacts CSV, skip header line. Loop through remaining lines of file. For each line, remove newline,
# strip quotes, split on commas and assign to corresponding vars. Create new dictionary with values from new vars,
# then add dictionary to contacts list. Close file when done.
with open('contacts_v1.csv', 'r+') as f:
    f.readline()
    for line in f:
        line = line.strip('\n')
        line = line.strip('"')
        name, fav_fruit, fav_color = line.split(',')
        new_dict = {'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color}
        contacts.append(dict(new_dict))
    f.close()


# Create function: Prompt for name, favorite fruit and favorite color. Create a new dictionary and populate it with
# prompts. Append list with new dictionary. Return done.
def create_repl():
    c_name = input('Enter a name: ')
    c_fav_fruit = input('Enter favorite fruit: ')
    c_fav_color = input('Enter favorite color: ')
    c_new_dict = {'name': c_name, 'favorite fruit': c_fav_fruit, 'favorite color': c_fav_color}
    contacts.append(dict(c_new_dict))
    return 'Done.'


# Read function: Prompt for name. Iterate through contacts list, if name matches name in prompt, return dictionary
# listing. Otherwise return not found.
def read_repl():
    input_name = input('Enter a name to search for: ')
    for item in contacts:
        if item['name'] == input_name:
            return item
    else:
        return 'Not found.'


# Update function: Prompt for name. Iterate through contacts in list, if name matches name in prompt, prompt for updated
# fruit and color. Update dictionary with new values and return done. Otherwise return not found.
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


# Delete function: Prompt for name. Iterate through contacts in list, if name matches name in prompt, remove item from
# list and return done. Otherwise return not found.
def delete_repl():
    input_name = input('Enter a name to delete: ')
    for item in contacts:
        if item['name'] == input_name:
            contacts.remove(item)
            return 'Done.'
    else:
        return 'Not found.'


# REPL loop: Prompt to create, read, update, delete or exit and call corresponding function, break loop on exit,
# otherwise print invalid input.
while True:
    u_input = input('Would you like to (c)reate, (r)ead, (u)pdate or (d)elete a record? Or (exit): ')
    if u_input == 'c':
        print(create_repl())
    elif u_input == 'r':
        print(read_repl())
    elif u_input == 'u':
        print(update_repl())
    elif u_input == 'd':
        print(delete_repl())
    elif u_input == 'exit':
        break
    else:
        print('Invalid input.')
