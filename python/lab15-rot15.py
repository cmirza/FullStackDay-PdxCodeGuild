'''
Lab 15 - ROT13 Cipher
'''


def rot13(text_in):  # define rot13 function
    text_out = ""  # define var for output string
    for char in text_in:  # begin looping through characters in string
        ord_char = ord(char)  # convert string to unicode value
        range = 123  # define upper bounds of character set
        bound = 97  # define lower bounds of character set
        new_char = (ord_char+13) % range  # add 13 to unicode ID of character
        if new_char < bound:  # if character value is outside lower bounds of character set, add bound to 'wrap' around
            new_char = new_char + bound
            text_out = text_out + chr(new_char)  # convert unicode value back to text
        else:
            text_out = text_out + chr(new_char)  # convert unicode value back to text
    return text_out  # return decoded text


value = "uryyb jbeyq"

print(rot13(value))  # pass list to function and print result
