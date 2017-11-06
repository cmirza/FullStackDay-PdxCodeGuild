'''
Lab 32 - Rain Data
Using matplotlib create a chart of the dates and the values.
'''

import datetime
import matplotlib.pyplot as plt


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


# rainiest year function, loops over rain data and creates a list of years measured and lists for totals, number of
# days and averages with the same number of entries. While looping over the length of the list of years, count the
# totals for each year and number of days, then calculate average for year. returns list of years and list of averages
def year_rain(dates):

    years = []
    totals = []
    num_days = []
    averages = []

    for day in dates:
        if day[0].year not in years:
            years.append(day[0].year)
            totals.append(0)
            num_days.append(0)
            averages.append(0)

    for i in range(len(years)):
        for day in dates:
            if day[0].year == years[i]:
                totals[i] += int(day[1])
                num_days[i] += 1
        averages[i] = totals[i]/num_days[i]

    return years, averages


# assign list of data to weather_data variable
weather_data = load_date()

rainiest_year = year_rain(weather_data)  # pass weather data to rainiest year function and assign result to variable

# assign years to x axis and averages to y axis, plot and show
x_values = rainiest_year[0]
y_values = rainiest_year[1]

plt.plot(x_values, y_values)
plt.show()
