'''
Lab 23 - Blackjack I
'''

card_values = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10}


def black_jack(crd1, crd2, crd3):
    crd_total = (card_values[crd1] + card_values[crd2] + card_values[crd3])
    print(crd_total)

    if crd_total > 21:
        print("Already busted")
    elif crd_total == 21:
        print("Blackjack!")
    elif crd_total >= 17:
        print("Stay")
    elif crd_total < 17:
        print("Hit")


while True:
    card_1 = input('What\'s your first card? ')
    if card_1 == 'done':
        break
    else:
        pass
    card_2 = input('What\'s your second card? ')
    if card_2 == 'done':
        break
    else:
        pass
    card_3 = input('What\'s your third card? ')
    if card_3 == 'done':
        break
    else:
        pass
    black_jack(card_1, card_2, card_3)
