import socket, threading
import pickle
import time
import sys
from Game import Game

LOCALHOST = "127.0.0.1"
PORT = 5050
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket, game):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)
        self.game = game
        self.sent_0= False

    def run(self, ):
        print("Connection from : ", clientAddress)

        msg = ''
        # self.csocket.send(pickle.dumps(""))
        while True:

            data = self.csocket.recv(2048)
            msg = pickle.loads(data)

            if msg == "done bidding":
                distribute("next section")


            if not self.sent_0:
                ids[0].send(pickle.dumps("first bidder"))
                self.sent_0 = True
            else:
                distribute(msg)

            if msg != "":
                print("from client", msg)

        print("done")

# TEST if the server will send the new value when it gets changed in pygame (no waiting for input on other clients)


        # print("Client at ", clientAddress, " disconnected...")
        # self.csocket.send(pickle.dumps("next"))
        #
        # while True:
        #     data = self.csocket.recv(1028)
        #     msg = pickle.loads(data)
        #     # if msg == 'bye':
        #     #   break
        #
        #     print("from client", msg)
        #     msg = game
        #     self.csocket.send(pickle.dumps(msg))


def distribute(data):
    if data == "playerid":
        for x in ids:
            x.send(pickle.dumps(x))

    else:
        for x in ids:
            x.sendall(pickle.dumps(data))
            time.sleep(.05)
    return ids


total = 0




def send_ids(num_players):
    index = 0
    while index < num_players:
        ids[index].send(pickle.dumps(index))
        index += 1


total_connections = 0
ids = []



#TOO CHANGE NUMBER OF PLAYERS, INCREASE THE 3 TO WHATEVER YOU NEED
while total_connections < 3:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    ids.append(clientsock)
    newthread = ClientThread(clientAddress, clientsock, 0)
    newthread.start()
    total_connections += 1
print(f"Total Players: {total_connections}")

game = Game(total_connections)
game.bidder = game.players[0]


def main():
    # game = Game(total_connections)
    game.deal()
    distribute(game)
    send_ids(total_connections)


if __name__ == '__main__':
    main()
