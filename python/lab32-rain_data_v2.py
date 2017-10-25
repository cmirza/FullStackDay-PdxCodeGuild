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


# rainiest year function, for each day in list of data, check if less than current year. If so, divide sum of rain for
# that year by number of days to get that years average. Then create new dict entry with current year as key and rain
# average as value. Otherwise iterate number of days, add amount of rain to rain total and set current year value. Once
# the loop finishes, create one more dictionary entry for the last year in list.
# then iterate over dictionary, check if the current entry's value is greater than the maximum value so far. If it is,
# assign key and value to variables. When done, return those variables.
def year_rain(dates):
    rain_avgs = {}
    current_year = 0
    num_days = 0
    sum_rain = 0

    for day in dates:
        if day[0].year < current_year:
            rain_year = sum_rain/num_days
            rain_avgs[current_year] = rain_year
            num_days = 0
            sum_rain = 0
        num_days += 1
        sum_rain += int(day[1])
        current_year = day[0].year
    rain_year = sum_rain / num_days
    rain_avgs[current_year] = rain_year

    max_rain = 0
    max_year = 0

    for year, rain in rain_avgs.items():
        if rain > max_rain:
            max_rain = rain
            max_year = year
    return max_year, max_rain


# assign list of data to weather_data variable
weather_data = load_date()

weather_avg = average(weather_data) # pass weather data to average function and assign result to variable
weather_var = variance(weather_data, weather_avg) # pass weather data to variance function and assign result to variable
rainiest_day = most_rain(weather_data) # pass weather data to most rain function and assign result to variable
rainiest_year = year_rain(weather_data) # pass weather data to rainiest year function and assign result to variable

# print out results
print('Average rainfall: ' + str(weather_avg))
print('Rainfall variance: ' + str(weather_var))
print(str(rainiest_day[0].month) + '/' + str(rainiest_day[0].day) + '/' + str(rainiest_day[0].year) + ' was the rainiest day.')
print(str(rainiest_year[0]) + ' was the rainiest year, with ' + str(rainiest_year[1]) + ' inchest of rain.')
