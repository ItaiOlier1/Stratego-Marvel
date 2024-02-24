import socket
import threading
from queue import Queue


class ClientComm:
    """
    class to represent client (communication)
    """

    def __init__(self, server_ip: str, port: int, msg_q: Queue):
        """
        init the object
        :param server_ip: server ip
        :param port: port of communication
        :param msg_q: the messages queue
        """
        self.socket = None  # the client socket
        self.server_ip = server_ip  # the server's ip
        self.port = port  # the communication port
        self.q = msg_q  # the queue of messages
        self._connect()  # connect to the server or close the program
        threading.Thread(target=self._main_loop, daemon=True).start()  # thread of getting messages

    def _connect(self):
        """
        connect to the server
        :return: None
        """
        self.socket = socket.socket()  # self socket
        # try to connect
        try:
            self.socket.connect((self.server_ip, self.port))
        except Exception as e:
            print("ClientComm - _main_loop", str(e))
            exit()

    def _main_loop(self):
        """
        connect to server
        :return: None
        """
        while True:
            try:
                length = int(self.socket.recv(4).decode())  # receive length
                data = self.socket.recv(length).decode()  # receive data
            except Exception as e:
                print("ClientComm - _main_loop", str(e))
                self.q.put("exit")
                exit()
            else:
                # if the server died, close
                if length == "":
                    exit()

                self.q.put(data)  # put the received data into the queue

    def send(self, msg):
        """
        sends a msg to the server
        :param msg: the message to send
        :return:
        """
        # encode the message
        if type(msg) == str:
            msg = msg.encode()

        # try to send the message
        try:
            self.socket.send(msg)
        except Exception as e:
            print("ClientComm - send", str(e))


