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


# define ascii barchart function
def ascii_barchart(num):
    for x in range(max(num), 0, -1):  # start loop for x coord
        print(end=' ')  # add extra space for alignment
        for y in num:  # start loop for drawing y coord
            if y >= x:  # if value of y is greater than or equal to x, print 'X' and suppress newline with space
                print("X ", end=' ')
            else:  # otherwise print ' '
                print("  ", end=' ')
        print()  # print newline
    print(num)  # print number list


# define list of numbers
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# pass list to functions and print results
ascii_barchart(data)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
