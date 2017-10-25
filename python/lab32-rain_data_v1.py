'''
Lab 32 - Rain Data
'''


# load_date function, opens input text, skips header line, for each line in file, strip newline, split on whitespace
# and add to new_list. When done, close file. In new_list, convert dates to datetime object and return new_list.
def load_date():
    with open('hayden_island.txt', 'r+') as file:
        file.readline()
        new_list = []
        for line in file:
            line = line.strip('\n')
            new_line = line.split()
            new_list.append(new_line)
        file.close()

        for list in new_list:
            list[0] = datetime.datetime.strptime(list[0], '%d-%b-%Y')
        return new_list

