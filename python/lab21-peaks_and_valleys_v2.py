'''
Lab 21 - Peaks and Valleys
Draw image of Xs using data list
'''


# define peaks function
def peaks(num):
    peak_list = []  # define peak list
    for i in range(1, len(num) - 1):
        if (num[i] > num[i - 1]) & (num[i] > num[i + 1]):
            peak_list.append(i)
    return peak_list


# define valleys function
def valleys(num):
    valley_list = []  # define valley list
    for i in range(1, len(num) - 1):
        if (num[i] < num[i - 1]) & (num[i] < num[i + 1]):
            valley_list.append(i)
    return valley_list


# define peaks and valleys function
def peaks_and_valleys(num):
    peak_and_valley_list = []  # define combined peak
    for i in range(1, len(num) - 1):
        if (num[i] > num[i - 1]) & (num[i] > num[i + 1]):
            peak_and_valley_list.append(i)
    for i in range(1, len(num) - 1):
        if (num[i] < num[i - 1]) & (num[i] < num[i + 1]):
            peak_and_valley_list.append(i)
    return sorted(peak_and_valley_list)


# define list of numbers
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# pass list to functions and print results
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
