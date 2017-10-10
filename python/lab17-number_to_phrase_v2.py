'''
Lab 17 - Number to Phrase
Handle numbers from 100-999.
'''


def num2phrs(num):

    words1 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    words2 = ['Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']

    if 1 <= num < 19:
        return words1[num-1]
    elif 20 <= num <= 99:
        tens_digit = num // 10
        ones_digit = num % 10
        return words2[tens_digit-2] + words1[ones_digit-1]
    elif 100 <= num <= 999:
        hundreds_digit = num // 100
        tens_digit = ((num // 10) % 10)
        ones_digit = num % 10
        return words1[hundreds_digit-1] + ' Hundred ' + words2[tens_digit-2] + words1[ones_digit-1]
    else:
        print("Invalid number.")


number = input('Enter a number between 0-999: ')
print(num2phrs(int(number)))
