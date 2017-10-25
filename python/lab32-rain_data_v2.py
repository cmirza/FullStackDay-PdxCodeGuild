'''
Lab 32 - Rain Data
Let's do some statistics...
'''

import datetime


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


# average function, for each item in list iterate total rain then divide by the number of dates to get the mean average
def average(dates):
    total = 0
    for day in dates:
        total += int(day[1])
    return total/len(dates)


# variance function, takes in list of rain data and mean average of rain. For each day in the list, subtract rain
# average from daily total, multiply that by itself and add it to a new total. Divide that total by the number of days
# to calculate variance.
def variance(dates, rain_avg):
    total = 0
    for day in dates:
        diff = float(day[1]) - rain_avg
        total += diff*diff
    return total/len(dates)


# day with most rain function, for each day in list of data, check if current day's rain is greater than previous
# greatest day of rain. It true, assign that day as greatest day variable. When done, return greatest day of rain
def most_rain(dates):
    rain_day = [0, 0]
    for day in dates:
        if int(day[1]) > int(rain_day[1]):
            rain_day = day
    return rain_day


# rainiest year function, loops over rain data and creates a list of years measured and lists for totals, number of
# days and averages with the same number of entries. While looping over the length of the list of years, count the
# totals for each year and number of days, then calculate average for year. Then find highest average in list and year
# with corresponding index. Then return max year and max average.
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

    max_average = max(averages)
    max_year = years[averages.index(max_average)]
    return max_year, max_average


# assign list of data to weather_data variable
weather_data = load_date()

weather_avg = average(weather_data)  # pass weather data to average function and assign result to variable
weather_var = variance(weather_data, weather_avg) # pass weather data to variance function and assign result to variable
rainiest_day = most_rain(weather_data)  # pass weather data to most rain function and assign result to variable
rainiest_year = year_rain(weather_data)  # pass weather data to rainiest year function and assign result to variable

# print out results
print('Average rainfall: ' + str(weather_avg))
print('Rainfall variance: ' + str(weather_var))
print(str(rainiest_day[0].month) + '/' + str(rainiest_day[0].day) + '/' + str(rainiest_day[0].year) + ' was the rainiest day.')
print(str(rainiest_year[0]) + ' was the rainiest year, with ' + str(rainiest_year[1]) + ' inchest of rain.')
