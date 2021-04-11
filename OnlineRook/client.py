import sys
import pygame
import socket
import pickle
import time
import os
from Player import Player
from Game import Game

SERVER = "127.0.0.1"
PORT = 5050
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("Connected")

pygame.init()

game = pickle.loads(client.recv(2048))
this_player = game.players[pickle.loads(client.recv(2048))]
card_images = []
window = pygame.display.set_mode((1450, 800))



assert isinstance(game, Game)
assert isinstance(this_player, Player)


def clearScreen():
    # pygame.display.set_mode((1450, 800)).fill((192, 192, 192))
    background()
    show_cards()


def adjustBid():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        this_player.bid += 5
        show_bidding()

    if pressed[pygame.K_DOWN]:
        this_player.bid -= 5
        show_bidding()


def sendBid():
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RETURN]:
        this_player.is_bidding = False
        clearScreen()
        show_bidding()
        # if this_player.bid > game.highest_bid:
        #     game.highest_bid = this_player.bid
        #     game.winning_bidder = this_player.name
        #     print("highest bid: " +str(game.highest_bid) + "\n"
        #           "winning bidder" + str(game.winning_bidder))
        return True


def background():
    size = width, height = 1450, 800
    color = (192, 192, 192)
    vel = [2, 2]
    title = "Rook"
    window = pygame.display.set_mode(size)
    font = pygame.font.Font('freesansbold.ttf', 32)
    pygame.display.set_caption(title)
    window.fill(color)
    # background
    window.blit(pygame.transform.scale(pygame.image.load("RookCardTemplates/Rookbackground.jpg"), size), (0, 0))

    # Title
    text = font.render('Multiplayer Rook', True, (0, 0, 0), (192, 192, 192))
    textRect = text.get_rect()
    textRect.center = (width // 2, 20)
    window.blit(text, textRect)
    # Main Deck thing
    card_back = pygame.image.load("RookCardTemplates/cardback.png")
    card_back = pygame.transform.scale(card_back, (170, 190))
    window.blit(card_back, (width // 2 - 100, height // 2 - 350))
    # Player names
    player_text = font.render(this_player.name, True, (0, 0, 0), (192, 192, 192))
    textRect2 = player_text.get_rect()
    textRect2.center = (width // 2, 750)
    window.blit(player_text, textRect2)


def discard():
    pressed = pygame.key.get_pressed()
    labels = ["q", "w", "e", "r", "t", "y"]
    labels2 = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="]
    pygame_keys = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y]

    # Kitty
    if this_player.cards_discarded < 6:

        if pressed[pygame.K_q] and game.kitty[labels.index("q")] not in game.kitty_discard_pile:
            game.kitty_discard_pile.append(game.kitty[labels.index("q")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_w] and game.kitty[labels.index("w")] not in game.kitty_discard_pile:
            game.kitty_discard_pile.append(game.kitty[labels.index("w")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_e] and game.kitty[labels.index("e")] not in game.kitty_discard_pile:
            game.kitty_discard_pile.append(game.kitty[labels.index("e")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_r] and game.kitty[labels.index("r")] not in game.kitty_discard_pile:
            game.kitty_discard_pile.append(game.kitty[labels.index("r")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_t] and game.kitty[labels.index("t")] not in game.kitty_discard_pile:
            game.kitty_discard_pile.append(game.kitty[labels.index("t")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_y] and game.kitty[labels.index("y")] not in game.kitty_discard_pile:
            game.kitty_discard_pile.append(game.kitty[labels.index("y")])
            this_player.cards_discarded += 1

        # Hand
        if pressed[pygame.K_BACKQUOTE] and this_player.hand[labels2.index("`")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("`")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_1] and this_player.hand[labels2.index("1")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("1")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_2] and this_player.hand[labels2.index("2")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("2")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_3] and this_player.hand[labels2.index("3")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("3")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_4] and this_player.hand[labels2.index("4")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("4")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_5] and this_player.hand[labels2.index("5")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("5")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_6] and this_player.hand[labels2.index("6")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("6")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_7] and this_player.hand[labels2.index("7")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("7")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_8] and this_player.hand[labels2.index("8")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("8")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_9] and this_player.hand[labels2.index("9")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("9")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_0] and this_player.hand[labels2.index("0")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("0")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_MINUS] and this_player.hand[labels2.index("-")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("-")])
            this_player.cards_discarded += 1

        if pressed[pygame.K_EQUALS] and this_player.hand[labels2.index("=")] not in game.hand_discard_pile:
            game.hand_discard_pile.append(this_player.hand[labels2.index("=")])
            this_player.cards_discarded += 1



    elif not this_player.choose_trump:
        # window.fill((192, 192, 192))
        background()
        # Showing Bid Num
        font = pygame.font.Font('freesansbold.ttf', 32)
        bid_text = font.render("Choose a Suit to be Trump", True, (0, 0, 0), (192, 192, 192))
        textRect2 = bid_text.get_rect()
        textRect2.center = (720, 500)
        window.blit(bid_text, textRect2)
        font = pygame.font.Font('freesansbold.ttf', 28)
        bid_text3 = font.render('1)Blue 2)Green, 3)Red, 4)Yellow', True, (0, 0, 0), (192, 192, 192))
        textRect3 = bid_text.get_rect()
        textRect3.center = (720, 450)
        window.blit(bid_text3, textRect3)
        if pressed[pygame.K_1]:
            game.trump = 'Blue'
            this_player.choose_trump = True
            time.sleep(.1)
        if pressed[pygame.K_2]:
            game.trump = 'Green'
            this_player.choose_trump = True
            time.sleep(.1)
        if pressed[pygame.K_3]:
            game.trump = 'Red'
            this_player.choose_trump = True
            time.sleep(.1)
        if pressed[pygame.K_4]:
            game.trump = 'Yellow'
            this_player.choose_trump = True
            time.sleep(.1)

    else:
        for x in game.hand_discard_pile:
            for y in this_player.hand:
                if str(x) == str(y):
                    this_player.hand.remove(y)
        for x in game.kitty_discard_pile:
            for y in game.kitty:
                if str(x) == str(y):
                    game.kitty.remove(y)
        this_player.hand = game.kitty + this_player.hand

        # client.sendall(pickle.dumps(this_player))
        window.fill((192, 192, 192))

        background()
        show_cards()
        game.discard_finished = True
        return True


def show_trick():
    label_index = 0
    labels2 = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="]
    x_cor = 450
    font = pygame.font.Font('freesansbold.ttf', 32)
    for val in game.this_trick:
        for x in card_images:
            text = str(val[1])
            to_remove = "layer"
            for char in to_remove:
                text = text.replace(char, "")
            if str(val[0].suit) == 'Bird':
                card_img = pygame.image.load("RookCardTemplates/RookBird.png")
                card_img = pygame.transform.scale(card_img, (100, 120))
                window.blit(card_img, (x_cor, 350))
                x_cor += 110
                label_index += 1
                if label_index < 14:
                    card_label = font.render(text, True, (0, 0, 0), (192, 192, 192))
                textRect3 = card_label.get_rect()
                textRect3.center = (x_cor - 50, 750)
                window.blit(card_label, (x_cor - 90, 310))

            if str(val[0].suit) + str(val[0].number) + '.png' == str(x):
                card_img = pygame.image.load("RookCardTemplates/" + str(x))
                card_img = pygame.transform.scale(card_img, (100, 120))
                window.blit(card_img, (x_cor, 350))
                x_cor += 110
                label_index += 1

                if label_index < 14:
                    card_label = font.render(text, True, (0, 0, 0), (192, 192, 192))
                textRect3 = card_label.get_rect()
                textRect3.center = (x_cor - 50, 750)
                window.blit(card_label, (x_cor - 90, 310))


def show_game():
    clearScreen()
    # Stats
    font = pygame.font.Font('freesansbold.ttf', 25)
    bid_text5 = font.render("Trump Suit: " + game.trump, True, (0, 0, 0), (192, 192, 192))
    textRect5 = bid_text5.get_rect()
    textRect5.center = (120, 20)
    window.blit(bid_text5, textRect5)

    bid_text6 = font.render("Trick " + str(game.trick_num) + "/" + str(game.num_cards), True, (0, 0, 0),
                            (192, 192, 192))
    textRect6 = bid_text6.get_rect()
    textRect6.center = (120, 40)
    window.blit(bid_text6, textRect6)

    show_trick()

    #print("this player: ", this_player)
    #print("gamecurrent : ", game.current_player)


    if str(this_player) == str(game.current_player):
        font = pygame.font.Font('freesansbold.ttf', 24)
        bidding_text = font.render("Play a card! "
                                   "Follow the first played card's suit if you are able to",
                                   True,
                                   (200, 0, 0), (192, 192, 192))
        textRect2 = bidding_text.get_rect()
        textRect2.center = (720, 525)
        window.blit(bidding_text, textRect2)
    else:
        font = pygame.font.Font('freesansbold.ttf', 24)
        bidding_text = font.render("Wait for your turn",
                                   True,
                                   (200, 0, 0), (192, 192, 192))
        textRect2 = bidding_text.get_rect()
        textRect2.center = (720, 525)
        window.blit(bidding_text, textRect2)


def show_hand_winner():
    hand_winner = game.players[0]
    for x in game.players:
        if x.points > hand_winner.points:
            hand_winner = x

    clearScreen()

    font = pygame.font.Font('freesansbold.ttf', 45)
    winner_text = font.render(str(hand_winner) + " Wins the hand!", True, (200, 0, 0), (192, 192, 192))
    textRect2 = winner_text.get_rect()
    textRect2.center = (720, 420)
    window.blit(winner_text, textRect2)
    game.current_player = str(hand_winner)

    points = []
    for x in game.players:
        points.append((str(x) + ":", x.points))
    print(points)

    font = pygame.font.Font('freesansbold.ttf', 30)
    winner_text4 = font.render(str(points), True, (200, 0, 0), (192, 192, 192))
    textRect4 = winner_text4.get_rect()
    textRect4.center = (720, 520)
    window.blit(winner_text4, textRect4)

    pygame.display.flip()


def show_game_winner():
    background()
    font = pygame.font.Font('freesansbold.ttf', 55)
    winner_text = font.render("GAME OVER! " + str(game.game_winner) + " WINS!", True, (200, 0, 0), (192, 192, 192))
    textRect2 = winner_text.get_rect()
    textRect2.center = (720, 420)
    window.blit(winner_text, textRect2)
    points = []
    for x in game.players:
        points.append((str(x) + ":", x.points))
    print(points)

    font = pygame.font.Font('freesansbold.ttf', 30)
    winner_text4 = font.render(str(points), True, (200, 0, 0), (192, 192, 192))
    textRect4 = winner_text4.get_rect()
    textRect4.center = (720, 540)
    window.blit(winner_text4, textRect4)

    pygame.display.flip()


def play_card():
    pressed = pygame.key.get_pressed()
    keys = [pygame.K_BACKQUOTE, pygame.K_1, pygame.K_2, pygame.K_3,
            pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
            pygame.K_9, pygame.K_0, pygame.K_MINUS, pygame.K_EQUALS]

    for x in keys:
        if pressed[x]:  # and this_player.hand[keys.index(x)] not in game.cards_played:
            game.cards_played.append(this_player.hand[keys.index(x)])

            # this_player.hand.remove(this_player.hand[keys.index(x)])
            this_player.played_card = this_player.hand[keys.index(x)]

            time.sleep(.15)
            #show_game()

            return True



def count_points():
    points_won = 0
    for x in game.players:
        for y in x.won_cards:
            x.points += y.get_points()

    if game.getPlayerObject(game.winning_bidder).points >= game.getPlayerObject(game.winning_bidder).bid:
        game.getPlayerObject(game.winning_bidder).points += game.getPlayerObject(game.winning_bidder).bid
    else:
        game.getPlayerObject(game.winning_bidder).points -= game.getPlayerObject(game.winning_bidder).bid

    for x in game.players:
        if x.points > 500:
            game.game_winner = x
            game.keep_playing = False




def get_trick_winner():


    lead_suit = game.this_trick[0][0].suit
    highest_card = game.this_trick[0][0]
    winning_player = game.this_trick[0][1]
    for x in game.this_trick:
        if x[0].suit == lead_suit:
            if x[0].get_value() > highest_card.get_value():
                highest_card= x[0]
                winning_player = x[1]

    for x in game.this_trick:
        if x[0].suit == game.trump:
            highest_card = x[0]
            winning_player = x[1]

    for x in game.this_trick:
        if x[0].suit == game.trump:
            if x[0].get_value() > highest_card.get_value():
                highest_card= x[0]
                winning_player = x[1]

    for x in game.this_trick:
        if x[0].get_value() == 20:
            winning_player = x[1]


    for x in game.players:
        if str(winning_player) == x.name:
            for y in game.this_trick:
                x.won_cards.append(y[0])

    for x in game.players:
        print()
        #print(x.won_cards)
    game.trick_winner = winning_player
    trick_over(winning_player)


def trick_over(winner):

    pygame.time.delay(1200)
    background()

    font = pygame.font.Font('freesansbold.ttf', 36)
    bidding_text = font.render(winner + " Takes the trick!", True,(200, 0, 0), (192, 192, 192))
    textRect2 = bidding_text.get_rect()
    textRect2.center = (720, 420)
    window.blit(bidding_text, textRect2)
    game.current_player = winner


def show_cards():
    label_index = 0
    labels = ["~", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="]
    x_cor = 10
    size = width, height = 1450, 800
    window = pygame.display.set_mode(size)
    font = pygame.font.Font('freesansbold.ttf', 32)

    # print(self.this_player.hand)
    for val in this_player.hand:
        if str(val.suit) == 'Bird':
            card_img = pygame.image.load("RookCardTemplates/RookBird.png")
            card_img = pygame.transform.scale(card_img, (100, 120))
            window.blit(card_img, (x_cor, 590))
            x_cor += 110
            label_index += 1
            if label_index < 14:
                card_label = font.render(labels[label_index - 1], True, (0, 0, 0), (192, 192, 192))
            textRect3 = card_label.get_rect()
            textRect3.center = (x_cor - 70, 750)
            window.blit(card_label, (x_cor - 70, 550))
        for x in card_images:
            if str(val.suit) + str(val.number) + '.png' == str(x):
                card_img = pygame.image.load("RookCardTemplates/" + str(x))
                card_img = pygame.transform.scale(card_img, (100, 120))
                window.blit(card_img, (x_cor, 590))
                x_cor += 110
                label_index += 1

                if label_index < 14:
                    card_label = font.render(labels[label_index - 1], True, (0, 0, 0), (192, 192, 192))
                textRect3 = card_label.get_rect()
                textRect3.center = (x_cor - 70, 750)
                window.blit(card_label, (x_cor - 70, 550))


def show_bidding():
    if game.bidder.name == this_player.name and this_player.is_bidding:
        window = pygame.display.set_mode((1450, 800))
        # Showing Bid Num
        font = pygame.font.Font('freesansbold.ttf', 32)
        bid_text = font.render("Current Bid: " + str(game.highest_bid), True, (0, 0, 0), (192, 192, 192))
        textRect2 = bid_text.get_rect()
        textRect2.center = (720, 500)
        window.blit(bid_text, textRect2)
        font = pygame.font.Font('freesansbold.ttf', 28)
        bid_text4 = font.render("Your Bid: " + str(this_player.bid), True, (0, 0, 0), (192, 192, 192))
        textRect4 = bid_text.get_rect()
        textRect4.center = (750, 390)
        window.blit(bid_text4, textRect4)

        # Bidding Text
        font = pygame.font.Font('freesansbold.ttf', 24)
        bid_text = font.render("Bid a number between the current bid and 200! Press Up to +5 and Down to -5, or Enter "
                               "to Pass", True,
                               (200, 0, 0), (192, 192, 192))
        bid_text2 = font.render("Press Spacebar to Shoot the Moon", True, (200, 0, 0), (192, 192, 192))
        textRect2 = bid_text.get_rect()
        textRect2.center = (720, 420)
        textRect3 = bid_text2.get_rect()
        textRect3.center = (720, 460)
        window.blit(bid_text, textRect2)
        window.blit(bid_text2, textRect3)
    else:
        size = width, height = 1450, 800
        window = pygame.display.set_mode(size)
        font = pygame.font.Font('freesansbold.ttf', 24)
        bidding_text = font.render("Wait for bidding to finish",
                                   True,
                                   (200, 0, 0), (192, 192, 192))
        textRect2 = bidding_text.get_rect()
        textRect2.center = (720, 420)
        window.blit(bidding_text, textRect2)


def show_kitty():
    label_index = 0
    labels = ["q", "w", "e", "r", "t", "y"]
    x_cor = 450
    font = pygame.font.Font('freesansbold.ttf', 32)
    # print(game.kitty)
    for val in game.kitty:
        if str(val.suit) == 'Bird':
            card_img = pygame.image.load("RookCardTemplates/RookBird.png")
            card_img = pygame.transform.scale(card_img, (100, 120))
            window.blit(card_img, (x_cor, 350))
            x_cor += 110
            label_index += 1
            if label_index < 14:
                card_label = font.render(labels[label_index - 1], True, (0, 0, 0), (192, 192, 192))
            textRect3 = card_label.get_rect()
            textRect3.center = (x_cor - 70, 750)
            window.blit(card_label, (x_cor - 70, 310))
        for x in card_images:
            if str(val.suit) + str(val.number) + '.png' == str(x):
                card_img = pygame.image.load("RookCardTemplates/" + str(x))
                card_img = pygame.transform.scale(card_img, (100, 120))
                window.blit(card_img, (x_cor, 350))
                x_cor += 110
                label_index += 1

                if label_index < 14:
                    card_label = font.render(labels[label_index - 1], True, (0, 0, 0), (192, 192, 192))
                textRect3 = card_label.get_rect()
                textRect3.center = (x_cor - 70, 750)
                window.blit(card_label, (x_cor - 70, 310))


def show_bid_winner():
    if game.winning_bidder == this_player.name:
        window = pygame.display.set_mode((1450, 800))
        font = pygame.font.Font('freesansbold.ttf', 24)
        bid_text = font.render(
            "You are the Bid Winner! Choose " + str(game.kitty_size - this_player.cards_discarded) + " cards "
                                                                                                     "to discard", True,
            (0, 0, 0),
            (192, 192, 192))
        textRect2 = bid_text.get_rect()
        textRect2.center = (720, 520)
        window.blit(bid_text, textRect2)

        show_cards()
        show_kitty()


    else:
        window = pygame.display.set_mode((1450, 800))
        font = pygame.font.Font('freesansbold.ttf', 30)
        bid_text = font.render("Waiting for the Bid Winner to finish... ",
                               True, (0, 0, 0), (192, 192, 192))
        textRect2 = bid_text.get_rect()
        textRect2.center = (720, 520)
        window.blit(bid_text, textRect2)


def datastream():
    send_game = False
    while True:
        sendBid()
        pygame.event.get()
        pygame.display.flip()

        in_data = pickle.loads(client.recv(2048))
        adjustBid()

        if isinstance(in_data, list):
            game.bidder = in_data[0]
            if game.current_bid < in_data[1]:
                game.highest_bid = in_data[1]
                game.winning_bidder = in_data[2]
            game.current_bid = in_data[1]
            # print("highest bid: " + str(game.highest_bid) + "\n"
            #            "winning bidder" + str(game.winning_bidder))

            clearScreen()
            show_bidding()

        if isinstance(in_data, tuple):
            game.bidding_done = True
            if game.current_bid < in_data[0]:
                game.highest_bid = in_data[0]
                game.winning_bidder = in_data[1]
            break

        # if in_data != "":
        #     print("From Server : ", in_data)

        if in_data == "first bidder":
            out_data = game
        if in_data == "done bidding":
            break
        elif sendBid():
            for x in game.players:
                if x.name == game.bidder.name:
                    if game.players.index(x) + 1 == len(game.players):
                        out_data = (this_player.bid, this_player.name)

                    else:
                        out_data = [game.players[game.players.index(x) + 1], this_player.bid, this_player.name]
            time.sleep(.25)
        else:
            out_data = ""
        client.sendall(pickle.dumps(out_data))

    if game.winning_bidder is None:
        game.highest_bid = this_player.bid
        game.winning_bidder = this_player.name

    window.fill((192, 192, 192))
    background()
    show_bid_winner()

    while True:
        # Bid Winner
        pygame.event.get()
        pygame.display.flip()
        in_data = pickle.loads(client.recv(2048))
        if in_data != "":
            print("From Server : ", in_data)

        if isinstance(in_data, list):
            for x in game.players:
                if x.name == in_data[0]:
                    x.hand = in_data[1]
                    game.trump = in_data[2]
                    window.fill((192, 192, 192))
                    # background()
                    # show_cards()
            break

        if not game.discard_finished:
            if discard():
                out_data = [this_player.name, this_player.hand, game.trump]
        else:
            out_data = ""
        client.sendall(pickle.dumps(out_data))

    for x in game.players:
        if x.name == game.winning_bidder:
            game.current_player = x



    background()
    show_cards()
    show_game()

    for x in game.players:
        if x.name == game.winning_bidder:
            index = game.players.index(x) + 1
    count = 0
    index = 0
    total_count = 0
    # Gameplay


    while game.keep_playing:
        # show_game()
        pygame.event.get()
        pygame.display.flip()
        in_data = pickle.loads(client.recv(2048))
        if in_data != "":
            print("From Server : ", in_data)
        out_data = ""

        if isinstance(in_data, tuple):
            index += 1
            count += 1


            if in_data not in game.this_trick:
                game.this_trick.append(in_data)
                for x in game.this_trick:
                    for y in this_player.hand:
                        if str(x[0]) == str(y):
                            this_player.hand.remove(y)

# HANDS END HERE

                if count == game.num_players:
                    total_count += 1
                    show_game()
                    pygame.display.flip()
                    get_trick_winner()
                    game.current_player = game.trick_winner
                    pygame.display.flip()
                    pygame.time.delay(2500)

                    count = 0
                    game.this_trick = []
                    game.trick_num += 1

                else:
                    try:
                        game.current_player = game.players[game.players.index(game.getPlayerObject(game.current_player))+1]
                    except:
                        game.current_player = game.players[0]

                if total_count == game.num_cards:
                    count_points()
                    show_hand_winner()
                    pygame.time.delay(2000)
                    game.deal()
                    #clearScreen()
                    #show_game()


                clearScreen()
                show_game()

        if str(game.current_player) == this_player.name:
            if play_card():

                out_data = (this_player.played_card, this_player.name)

        client.sendall(pickle.dumps(out_data))

    while True:
        pygame.display.flip()
        show_game_winner()
        pygame.event.get()


    client.close()


def main():
    path = 'RookCardTemplates'
    for x in os.listdir(path):
        if x.endswith('.png'):
            card_images.append(x)
    print(this_player.name)

    # display()
    background()
    show_cards()
    show_bidding()
    client.sendall(pickle.dumps(""))
    time.sleep(.1)
    datastream()


if __name__ == '__main__':
    main()
