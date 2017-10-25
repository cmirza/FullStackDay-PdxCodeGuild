'''
Lab 32 - Rain Data
Let's do some statistics...
'''

import datetime


def load_date():
    with open('hayden_island.cst', 'r+') as file:
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


def average(dates):
    total = 0
    for day in dates:
        total += int(day[1])
    return total/len(dates)


def variance(dates, rain_avg):
    total = 0
    for day in dates:
        diff = float(day[1]) - rain_avg
        total += diff*diff
    return total/len(dates)


def most_rain(dates):
    rain_day = [0, 0]
    for day in dates:
        if int(day[1]) > int(rain_day[1]):
            rain_day = day
    return rain_day


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
            pass
        num_days += 1
        sum_rain += int(day[1])
    return rain_avgs

weather_data = load_date()

weather_avg = average(weather_data)
weather_var = variance(weather_data, weather_avg)
rainiest_day = most_rain(weather_data)
rainiest_year = year_rain(weather_data)

print('Average rainfall: ' + str(weather_avg))
print('Rainfall variance: ' + str(weather_var))
print(str(rainiest_day[0].month) + '/' + str(rainiest_day[0].day) + '/' + str(rainiest_day[0].year) + ' was the rainiest day.')
print(rainiest_year)
