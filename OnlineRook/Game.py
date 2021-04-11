import random
from Player import Player
from Deck import Deck
from Card import Card


class Game:
    def __init__(self, num_players):
        self.num_cards = 0
        self.num_players = num_players
        self.deck = Deck()
        self.players = []
        self.kitty = []
        self.kitty_size = 0
        self.current_bid = 80
        self.winning_bidder = None
        self.highest_bid = 80
        self.last_bidder = None
        self.bidding_done = False
        self.bidder = None
        self.kitty_discard_pile = []
        self.hand_discard_pile = []
        self.discard_finished = False
        self.trump = None
        self.trick_num = 1
        self.cards_played = []
        self.current_player = ''
        self.trick_winner = ''
        self.this_trick = []
        self.keep_playing = True
        self.game_winner = ''

        # self.trick_winner = "Player 1"



        for x in range(1, int(num_players) + 1):
            self.players.insert(0, Player(x))

        # self.deal()

    def deal(self):
        self.deck.populate_deck(self.num_players)
        self.make_kitty()
        self.num_cards = (len(self.deck.cards) // self.num_players)
        for player in self.players:

            for x in range(1, (self.num_cards + 1)):
                card_dealt = random.choice(self.deck.cards)
                player.hand.insert(0, card_dealt)
                self.deck.cards.remove(card_dealt)
        print("Dealing complete")

    def make_kitty(self):

        if self.num_players == 3:
            self.kitty_size = 6
            for x in range(6):
                dealt_card = random.choice(self.deck.cards)
                self.kitty.insert(0, dealt_card)
                self.deck.cards.remove(dealt_card)

        elif self.num_players == 4:
            self.kitty_size = 5
            for x in range(5):
                dealt_card = random.choice(self.deck.cards)
                self.kitty.insert(0, dealt_card)
                self.deck.cards.remove(dealt_card)

        elif self.num_players == 5:
            self.kitty_size = 4
            for x in range(4):
                dealt_card = random.choice(self.deck.cards)
                self.kitty.insert(0, dealt_card)
                self.deck.cards.remove(dealt_card)

        elif self.num_players == 6:
            self.kitty_size = 3
            for x in range(3):
                dealt_card = random.choice(self.deck.cards)
                self.kitty.insert(0, dealt_card)
                self.deck.cards.remove(dealt_card)

    # def bid(self):
    #     i = 0
    #     print("Current Bid: " + str(self.current_bid))
    #     while i < len(self.players):
    #         current_bidder = self.players[i]
    #         current_bidder.bid = (input(str(current_bidder) + "\n" + "Bid a Number Between " + str(
    #             self.current_bid + 5) + " and 200, or 'Pass':"))
    #         if current_bidder.bid != "Pass":
    #             current_bidder.bid = int(current_bidder.bid)
    #             self.current_bid = current_bidder.bid
    #             self.winning_bidder = current_bidder
    #         i += 1
    #         print()
    #         print("Current Bid: " + str(self.current_bid))
    #
    #     # find winning bidder
    #
    #     print()
    #     self.winning_bidder.hand = self.winning_bidder.hand + self.kitty
    #     print("Winning Bidder: " + str(self.winning_bidder) + " Receives the Kitty")

    def getPlayerObject(self, player_check):
        for x in self.players:
            if str(x) == str(player_check):
                return x
    def __str__(self):
        if self.bidding_done == False:
            return "Current Bid is " + str(self.current_bid) + "\n" + "Current Bidder is " + str(self.bidder)

    def play(self):
        self.deal()
