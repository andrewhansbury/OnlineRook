class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def get_value(self):
        if self.number == 0:
            return 20
        elif self.number == 1:
            return 19
        else:
            return self.number


    def get_points(self):

        if self.number == 5:
            return 5
        elif self.number == 10:
            return 10
        elif self.number == 14:
            return 10
        elif self.number == 1:
            return 15
        elif self.number == 0:
            return 20
        else:
            return 0

    def __repr__(self):
        if self.number == 0:
            return "Rook Bird"
        else:
            return str(self.number) + " of " + self.suit

    def __str__(self):
        if self.number == 0:
            return "Rook Bird"
        else:
            return str(self.number) + " of " + self.suit