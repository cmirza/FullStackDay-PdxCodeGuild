'''
Crime Data
'''


import datetime


# load the crime data file, skip header line, strip newline, split by comma, append to new list and close file.
# Turn date field into an object and return the list.
def load_crime():
    with open('crime_data.csv', 'r+') as file:
        file.readline()
        new_list = []
        for line in file:
            line = line.strip('\n')
            new_line = line.split(',')
            new_list.append(new_line)
        file.close()

        for crime in new_list:
            crime[5] = datetime.datetime.strptime(crime[5], '%m/%d/%y')

        return new_list


# top crime function. loops over the list to make a list of crimes and a list of years measured. While looping
# over types of crimes, loop over the crimes to count types of crimes that occurred. While looping over the years of
# crime measured, count the occurrences of crime for each year. Then return what crime occurred the most and how much,
# what crime occurred the least and how much and what year had the most crime and by how much.
def top_crime(crimes):
    crime_type = []
    crime_count = []
    crime_year = []
    crime_year_count = []

    for crime in crimes:
        if crime[8] not in crime_type:
            crime_type.append(crime[8])
            crime_count.append(0)
        if crime[5].year not in crime_year:
            crime_year.append(crime[5].year)
            crime_year_count.append(0)

    for i in range(len(crime_type)):
        for crime in crimes:
            if crime[8] == crime_type[i]:
                crime_count[i] += 1

    for i in range(len(crime_year)):
        for crime in crimes:
            if crime[5].year == crime_year[i]:
                crime_year_count[i] += 1

    max_count = max(crime_count)
    max_crime = crime_type[crime_count.index(max_count)]

    min_count = min(crime_count)
    min_crime = crime_type[crime_count.index(min_count)]

    max_crime_year_count = max(crime_year_count)
    max_crime_year = crime_year[crime_year_count.index(max_crime_year_count)]

    return max_crime, max_count, min_crime, min_count, max_crime_year, max_crime_year_count


# instantiate load crime and top crime function
crime_stats = load_crime()
most_crime = top_crime(crime_stats)

# print results
print('The most common crime in South Portland is ' + str(most_crime[0]) + ', which happened ' + str(most_crime[1])+' times.')
print('The least common crime in South Portland is ' + str(most_crime[2]) + ', which happened ' + str(most_crime[3])+' times.')
print(str(most_crime[4]) + ' had the most crime, with ' + str(most_crime[5])+' instances.')
