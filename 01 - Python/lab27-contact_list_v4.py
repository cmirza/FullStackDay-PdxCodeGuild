'''
Lab 27 - Contact List
Add a phone number column to the CSV, with each contact's phone number
Use the Twilio API to send SMS messages from the terminal
'''


from twilio.rest import Client  # import library for Twilio API


contacts = []  # define contacts list

# Open contacts CSV, skip header line. Loop through remaining lines of file. For each line, remove newline,
# strip quotes, split on commas and assign to corresponding vars. Create new dictionary with values from new vars,
# then add dictionary to contacts list. Close file when done.
with open('contacts_v2.csv', 'r+') as f:
    f.readline()  # skip first line
    for line in f:  # loop through each line of csv
        line = line.strip('\n')  # remove newline
        line = line.strip('"')  # strip quotes
        name, fav_fruit, fav_color, p_num = line.split(',')  # split on comma and assign to vars
        new_dict = {'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color, 'phone number': p_num}  # create dictionary
        contacts.append(dict(new_dict))  # add dictionary to list
    f.close()  # close file


# Create function: Prompt for name, favorite fruit and favorite color. Create a new dictionary and populate it with
# prompts. Append list with new dictionary. Return done.
def create_repl():
    c_name = input('Enter a name: ')
    c_fav_fruit = input('Enter favorite fruit: ')
    c_fav_color = input('Enter favorite color: ')
    c_p_num = input('Enter phone number:')
    c_new_dict = {'name': c_name, 'favorite fruit': c_fav_fruit, 'favorite color': c_fav_color, 'p_num': c_p_num}
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
            u_p_num = input('Enter updated phone number:')
            item['favorite fruit'] = u_fav_fruit
            item['favorite color'] = u_fav_color
            item['phone number'] = u_p_num
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


# SMS function: Prompt for name. Iterate through contacts in list, if name matches name in prompt, set phone number var
# and prompt for message to send. Then call Twilio API to send message and return sent. Otherwise return not found.
def sms_twilio():
    account_sid = "AC89d0fd5dff581ec57fe20430868376b5"
    auth_token = "b15cccb7a26aa86b42a5f14ebccf23cf"
    client = Client(account_sid, auth_token)

    input_name = input('Enter a name you\'d like to text: ')
    for item in contacts:
        if item['name'] == input_name:
            sms_p_num = item['phone number']
            sms_msg = input("Enter your message: ")
            message = client.api.account.messages.create(to=sms_p_num, from_="+19718033720", body=sms_msg)
            return 'Sent.'
    else:
        return 'Not found.'


# REPL loop: Prompt to create, read, update, delete or exit and call corresponding function. On exit, open contacts csv,
# write header on first line, for each item in contacts list, print each key of dictionary seprated by comma, ending
# with new line, closing file afterwards. Otherwise print invalid input.
while True:
    u_input = input('Would you like to (c)reate, (r)ead, (u)pdate or (d)elete a record? Also (t)ext someone or (exit): ')
    if u_input == 'c':
        print(create_repl())
    elif u_input == 'r':
        print(read_repl())
    elif u_input == 'u':
        print(update_repl())
    elif u_input == 'd':
        print(delete_repl())
    elif u_input == 't':
        print(sms_twilio())
    elif u_input == 'exit':
        with open('contacts_v1.csv', 'w+') as f:
            f.write('Name,Favorite Fruit,Favorite Color,Phone Number\n')
            for item in contacts:
                f.write(item['name']+','+item['favorite fruit']+','+item['favorite color']+item['phone number']+'\n')
        break
    else:
        print('Invalid input.')
