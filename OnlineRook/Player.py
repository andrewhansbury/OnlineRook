class Player:
    def __init__(self, player_num):
        self.is_dealer = False
        self.player_num = player_num
        self.hand = []
        self.points = 375
        self.bid = 80
        self.name = "Player " + str(self.player_num)
        self.is_bidding = True
        self.discard_pile = []
        self.cards_discarded = 0
        self.choose_trump = False
        self.played_card = None
        self.won_cards = []


    def set_is_dealer(self, value):
        self.is_dealer = value

    def __str__(self):
         return "Player " + str(self.player_num)
# + "\n" + "Hand: " + str(self.hand)