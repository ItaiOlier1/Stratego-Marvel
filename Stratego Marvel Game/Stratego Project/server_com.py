import socket
import threading
import select
from queue import Queue
from game import Game, Games


games = Games()  # an object of games


class ServerComm:
    """
        class to represent server (communication)
    """
    def __init__(self, port: int, msg_q: Queue):
        """
        constructor:
        :param port: the communication port
        :param msg_q: the queue message
        """
        self.socket = None  # the communication server socket
        self.port = port  # the port of the communication
        self.q = msg_q  # the queue of the messages
        self.open_clients = {}  # the clients dict

        threading.Thread(target=self._main_loop).start()  # thread of receiving messages

    def _main_loop(self):
        """
        connect to client and receive messages
        :return:
        """
        self.socket = socket.socket()
        self.socket.bind(('0.0.0.0', self.port))
        self.socket.listen(4)

        while True:
            # use select to overcome blocking
            rlist, wlist, xlist = select.select([self.socket] + list(self.open_clients.keys()), list(self.open_clients.keys()), [])
            # run over the sockets in the rlist
            for current_socket in rlist:
                # if the sockets are equals, there is a new client who tries to connect to the server
                if current_socket is self.socket:
                    client, addr = self.socket.accept()  # accept the connection
                    ip = addr[0]
                    print(f'{ip} - connected')
                    print(client)
                    self.open_clients[client] = ip  # add the new client to the clients dict by the ip and socket

                    # if the current player has no game to join, create a new game
                    if games.amount_of_users % 2 == 0:
                        games.amount_of_games += 1
                        game = Game(games.amount_of_games)
                        game.add_player(ip)  # add a player
                        games.games_list.append(game)  # create a new game with the player
                        print("ip - ", ip)
                        print("\ncreate a new game")
                    else:
                        # add the current player to a game
                        games.games_list[-1].add_player(ip)  # add the player with his address
                        print(games.games_list[-1].player2.getIP())
                        print("ip - ", ip)
                        print("\nadd player number two to the game")

                    # add a player to a game:
                    games.amount_of_users += 1

                else:
                    # try to receive data
                    try:
                        length = int(current_socket.recv(3).decode())  # receive the length
                        data = current_socket.recv(length).decode()  # receive the data
                    except Exception as e:
                        print("ServerComm - _main_loop", str(e))
                        self._disconnect_client(current_socket)  # disconnect client
                    else:
                        if data == '':
                            self._disconnect_client(current_socket)  # disconnect client
                        else:
                            self.q.put((self.open_clients[current_socket], data))  # put the data in the queue

    def send_specific_client(self, data, ip: str):
        """
        send to a specific client a message
        :param data: the data to send
        :param ip: the ip of the client to send to
        :return: None
        """
        # decode data
        if type(data) == str:
            data = data.encode()
        length = str(len(data)).zfill(4).encode()  # length of data
        for soc in self.open_clients.keys():
            if self.open_clients[soc] == ip:
                try:
                    soc.send(length + data)
                except Exception as e:
                    print("ServerComm - send_specific_client", str(e))
                    self._disconnect_client(soc)

    def _disconnect_client(self, client_socket):
        """
        dissconnect a client from the server
        :param client_socket: the socket to disconnect
        :return: None
        """
        if client_socket in self.open_clients.keys():
            games.amount_of_games -= 1
            games.amount_of_users -= 1

            print("amount_of_games - ", games.amount_of_games)
            print("amount_of_users - ", games.amount_of_users)

            print(f'{self.open_clients[client_socket]} - disconnected')
            del self.open_clients[client_socket]
            client_socket.close()
