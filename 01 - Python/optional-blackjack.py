'''
Blackjack
'''

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                c = Card(rank, suit)
                self.cards.append(f'{c.rank} of {c.suit}')

    def shuffle(self):
        random.shuffle(self.cards)

    def deck_cut(self):
        cut_point = random.randint(4, 47)
        top_cards = self.cards[0:cut_point]
        bottom_cards = self.cards[cut_point:]
        bottom_cards.extend(top_cards)
        self.cards = bottom_cards

    def __len__(self):
        return len(self.cards)

    def draw_card(self):
        return self.cards.pop()


deck_rank = Deck(rank)
deck_suit = Deck(suit)
cards = Card(deck_rank, deck_suit)

print(deck.shuffle())

