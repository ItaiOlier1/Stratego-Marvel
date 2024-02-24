
class Game:

    # constructor:
    def __init__(self,  game_id):
        """
        constructor
        :param game_id: the id of the game
        """
        self.id = game_id  # the id of the game
        self.player1 = None  # player 1
        self.player2 = None  # player 2
        self.board_dict = self._create_board_dict()  # board dict
        self.connected_clients = 0  # connected clients

    def _create_board_dict(self):
        """
        :return: the game board dict
        """
        self.board_dict = {}  # create the board dict
        # init the boar dict
        for rect in range(0, 100):
            self.board_dict[rect] = None
        return self.board_dict

    def add_player(self, address):
        """
        add a player to the game
        :param address: the ip address of the player
        :return:
        """
        # if there are less then 2 clients connected
        if self.connected_clients < 2:
            if self.connected_clients == 0:
                self.player1 = Player(address, 1)
                self.connected_clients += 1
                print("player 1 connected")
            else:
                self.player2 = Player(address, 2)
                self.connected_clients += 1
                print("player 2 connected")


class Player:

    # constructor:
    def __init__(self, ip, player_number):
        """
        constructor
        :param ip: the ip address of this user
        :param player_number: the number of the player
        """
        self.ip = ip  # the ip address of the user
        self.player_number = player_number  # the player number
        self.player_name = ""  # the nickname of the player

    def setPlayer_number(self, num):
        """
        set the player's number
        :param num: the number
        :return: None
        """
        self.player_number = num

    def getPlayer_number(self):
        """
        get the player's number
        :return: the player's number
        """
        return self.player_number

    def getIP(self):
        """
        get the ip address
        :return: the ip
        """
        return self.ip

    def getPlayer_name(self):
        """
        get the player's nickname
        :return: nickname
        """
        return self.player_name

    def setPlayer_name(self, name):
        """
        set the players nickname
        :param name: the nickname
        :return: the players nickname
        """
        self.player_name = name


class Games:

    # constructor:
    def __init__(self):
        """
        constructor
        """
        self.games_list = []  # the games list
        self.amount_of_games = 0  # the amount of games
        self.amount_of_users = 0  # the amount of users





