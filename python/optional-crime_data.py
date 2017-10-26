'''
Crime Data
'''

ef load_date():
    with open('crime_data.csv', 'r+') as file:
        file.readline()
        new_list = []
        for line in file:
            line = line.strip('\n')
            new_line = line.split(',')
            new_list.append(new_line)
        file.close()

        for list in new_list:
            list[0] = datetime.datetime.strptime(list[0], '%d-%b-%Y')
        return new_list

