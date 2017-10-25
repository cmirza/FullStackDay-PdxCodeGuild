'''
Blackjack
'''

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)

    def cut(self):
        cut_point = random.randint(4, 46)
        top_cards = self.cards[0:cut_point]
        bottom_cards = self.cards[cut_point:]
        bottom_cards.extend(top_cards)
        self.cards = bottom_cards

    def __len__(self):
        return len(self.cards)

    def draw_card:



deck = Deck()

for card in deck.cards:
    print(card)