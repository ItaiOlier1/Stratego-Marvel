
import threading
import select
from queue import Queue


class Communication:

    # constructor:
    def __init__(self, server_soc, port: int, msg_q: Queue, open_clients, ip1, ip2):
        """
        constructor:
        :param server_soc:  the socket of the server
        :param port: the connection port
        :param msg_q: the queue for the messages
        :param open_clients: a dict of the connected clients
        :param ip1: ip address of player
        :param ip2: ip address of player
        """
        self.socket = server_soc
        self.port = port
        self.q = msg_q
        self.open_clients = open_clients
        self.ip1 = ip1
        self.ip2 = ip2

        # threading to receive data
        threading.Thread(target=self._main_loop).start()

    def _main_loop(self):
        """
        the main loop of the communication
        receive data from connected clients
        :return:
        """
        while True:
            # use select to overcome blocking
            rlist, wlist, xlist = select.select([self.socket] + list(self.open_clients.keys()), list(self.open_clients.keys()), [])
            for current_socket in rlist:
                try:
                    length = int(current_socket.recv(3).decode())  # receive the length
                    data = current_socket.recv(length).decode()  # receive the data
                except Exception as e:
                    print("game_com - _main_loop", str(e))
                    self._exception_disconnect(current_socket)  # disconnect client
                else:
                    if data == '':
                        self._exception_disconnect(current_socket)  # disconnect client

                    else:
                        self.q.put((self.open_clients[current_socket], data))  # put data in the queue

    def _exception_disconnect(self, current_socket):
        """
        if a user has a problem and we need to disconnect the 2 clients
        and to send the second client that he wins
        :param current_socket: the current socket to disconnect
        :return: None
        """
        print("game_com - _main_loop - _exception_disconnect")

        ip = self.open_clients[current_socket]  # get current ip
        print("ip1 - " + ip)

        # get the ip to send to that he is the winner (the second client)
        if ip == self.ip1:
            ip = self.ip2
        else:
            ip = self.ip1

        print("ip2 - " + ip)

        # send to the second client that he is the winner
        self.send_specific_client("11w", ip)

        # disconnect the first client
        self._disconnect_client(current_socket)

    def send_specific_client(self, data, ip: str):
        """
        send a message to a specific client
        :param data: the data to send
        :param ip: the ip to send to
        :return: None
        """
        # encode the data
        if type(data) == str:
            data = data.encode()
        length = str(len(data)).zfill(4).encode()  # get the length of the data
        for soc in self.open_clients.keys():
            if self.open_clients[soc] == ip:
                try:
                    soc.send(length + data)  # send
                except Exception as e:
                    print("ServerComm - send_specific_client ", str(e))
                    self._disconnect_client(soc)  # disconnect the client (by the socket)

    def _disconnect_client(self, client_socket):
        """
        disconnect a client
        :param client_socket:
        :return:
        """
        # if the socket is exist, disconnect the client:
        if client_socket in self.open_clients.keys():
            print(f'{self.open_clients[client_socket]} - disconnected')
            del self.open_clients[client_socket]  # delete from the connected to the game list
            client_socket.close()  # close the connection
