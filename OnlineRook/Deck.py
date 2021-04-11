from Card import Card
import random
class Deck:
    def __init__(self):
        self.suits = ['Blue', 'Green', 'Red', 'Yellow']
        self.cards = []

    def populate_deck(self, num_players):
        if 3 <= num_players <= 6:
            for i in self.suits:
                for x in range(1, 15):
                    if x != 2 and x != 3 and x != 4:
                        self.cards.insert(0, Card(x, i))

        else:
            for i in self.suits:
                for x in range(1, 15):
                    self.cards.insert(0, Card(x, i))
        self.cards.insert(0, Card(0,"Bird"))

    def __repr__(self):
        return str(self.cards)

    def print_deck(self):
        for x in self.cards:
            print(str(x))