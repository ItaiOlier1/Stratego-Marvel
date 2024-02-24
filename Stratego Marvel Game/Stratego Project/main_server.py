import queue
from server_com import *
from game import Game
from game_com import Communication

reverse_board_dict_values = {}  # create the mirror reverse dict values

# create the reverse_board_dict_values dict with the reverse values
for rect_num in range(100):
    reverse_board_dict_values[rect_num] = 99 - rect_num
print(reverse_board_dict_values)

recv_q = queue.Queue()  # the queue that saves the server's received information
comm = ServerComm(1000, recv_q)  # the communication object of the server


def handle_msgs(the_comm, queue_comm, game: Game):
    """
    handle received messages
    :param the_comm: the communication object
    :param queue_comm: the queue with the data
    :param game: the game (if there is)
    :return: None
    """
    while True:
        ip, data = queue_comm.get()
        handle_msg_by_command_number(data, ip, game, the_comm)  # handle messages by the command number


def handle_msg_by_command_number(data, ip, game: Game, the_comm):
    """
    handle messages by command number
    :param data: the data
    :param ip: the ip of the sender of the command
    :param game: the game of the sender (if there is)
    :param the_comm: the communication obj
    :return: None
    """
    command_number, data = int(data[:2]), str(data[2:])  # split the data to command number and the data
    print("command_number " + str(command_number))
    print("data - " + data)

    # check the command number:

    # if command number is 1
    if command_number == 1:
        create_game(data, ip)  # save the new data of the client in the game

    # if command number is 2
    if command_number == 2:
        handleTurn(data, ip, game, the_comm)  # handle a turn


def create_game(data, ip):
    """
    create the game and gave the new data at the game
    , after there will be two players in the game, start the game
    :param data: the data (nickname, game board)
    :param ip: the ip address of the sender
    :return: None
    """
    game = games.games_list[-1]  # the current game is the last game in the list

    # split the data:

    len_nickname = int(data[:2])  # get the length of the nickname
    nickname = str(data[2:len_nickname + 2])  # get the nickname
    data = str(data[2 + len(nickname):])  # get the data (game board string)

    print("len - " + str(len_nickname))
    print("nickname - " + nickname)
    print("data - " + data)

    # set the sender nickname by the ip
    if game.player1.getIP() == ip:
        game.player1.setPlayer_name(nickname)
    else:
        game.player2.setPlayer_name(nickname)

    rect_and_card_list = data.split("@")  # split every rect with card in to a list

    reverse = game.board_dict[60] is not None  # if there is already a player in the game, turn on the reverse flag

    # run over the list of rectangles and cards numbers and set the boards:
    for rect_and_card in rect_and_card_list:
        rect_and_card_split = rect_and_card.split("$")

        # split the rect number and the card number:
        rect_number, card_num = int(rect_and_card_split[0]), rect_and_card_split[1]

        # set the location in the board by the reverse flag
        if not reverse:
            game.board_dict[rect_number] = card_num, str(ip)
        else:
            rect_number = get_reverse_rect_number(rect_number)
            game.board_dict[rect_number] = card_num, str(ip)
    print(game.board_dict)

    # if the second player joined, disconnect from the server_com and start the game
    if reverse:
        player2_name = str(game.player2.getPlayer_name())  # set the nickname of player 2

        # send to the first client
        comm.send_specific_client \
            ("01" + str(len(player2_name)).zfill(2) + str(player2_name) +
             str(game.player1.getPlayer_number()), game.player1.getIP())  # send to player 1

        player1_name = str(game.player1.getPlayer_name())  # set the nickname of player 1

        # send to the second client
        comm.send_specific_client \
            ("01" + str(len(player1_name)).zfill(2) + str(player1_name) +
             str(game.player2.getPlayer_number()), game.player2.getIP())  # send to player 2

        print("Board - " + str(game.board_dict))

        ip_1 = game.player1.getIP()
        ip_2 = game.player2.getIP()
        print(ip_1)  # print player 1 ip address
        print(ip_2)  # print player 2 ip address

        clients_soc_dict = {}

        print(comm.open_clients)

        # delete the two clients from the server com open_clients list:
        # (the communication needs to be inside the game):
        for key, value in comm.open_clients.items():
            print("val - ", value)
            if value == ip_1:
                clients_soc_dict[key] = value
                del comm.open_clients[key]  # delete
                break
        for key, value in comm.open_clients.items():
            if value == ip_2:
                clients_soc_dict[key] = value
                del comm.open_clients[key]  # delete
                break
        print(f"{ip_1} , {ip_2} deleted from the main server")
        print(f"the open clients dict now: {comm.open_clients}")

        # create the game:
        threading.Thread \
            (target=main_game, args=(game, comm.socket, comm.port, clients_soc_dict, ip_1, ip_2), daemon=True).start()


def main_game(game: Game, server_soc, port: int, open_clients, ip_addr1, ip_addr2):
    """
    the main game def
    receive information from the clients and handle it
    :param game: the game object
    :param server_soc: the socket of the server
    :param port: the communication port
    :param open_clients: the connected clients to the game (dict with soc and ip)
    :param ip_addr1: ip address
    :param ip_addr2: ip address
    :return: None
    """
    game_queue = queue.Queue()  # the game queue
    game_comm = Communication(server_soc, port, game_queue, open_clients, ip_addr1, ip_addr2)  # create a game comm obj
    threading.Thread(target=handle_msgs, args=(game_comm, game_queue, game), daemon=True).start()  # receive information


def get_reverse_rect_number(rect_number):
    """
    get the reverse value for the rect number that was given
    :param rect_number: the rect number to find the reverse value of
    :return: the reverse rect number
    """
    return reverse_board_dict_values[int(rect_number)]


def move(old_rect_num, new_rect_num, game: Game):
    """
    move a card from old place to new place
    :param old_rect_num: the number of the source rect
    :param new_rect_num: the number of the destination rect
    :param game: the game obj
    :return: None
    """
    card_num_and_ip = game.board_dict[old_rect_num]  # the card number and the ip
    game.board_dict[old_rect_num] = None  # set the old place as None
    game.board_dict[new_rect_num] = card_num_and_ip  # set the new place with the 'card_num_and_ip'


def get_second_client_ip(ip, game):
    """
    get the second (waiting) client's ip by the ip argument
    :param ip: the ip of one of the clients
    :param game: the game object
    :return: the another ip address
    """
    if ip == game.player2.getIP():
        ip = game.player1.getIP()
    else:
        ip = game.player2.getIP()
    return ip


def get_waiting_client_ip_and_update_rectangles(ip, game, old_rect_num, new_rect_num):
    """
    this def gets an ip of the sender of a turn, the def will get the second client's ip to send the turn to him
    and will switch the old and new rect numbers to the reverse numbers because the goal is to send the waiting client
    (who didn't made his turn yet) the enemy's turn with the right variables

    if the second client is reversed, don't reverse the variables of the rect numbers. else, reverse.

    :param ip: the ip of the sender of the turn
    :param game: the game obj
    :param old_rect_num: the old rectangle number
    :param new_rect_num: the enw rectangle number

    :return: the ip address and the new rectangles numbers
    """
    # check who is the client to send to the data by checking and comparing the senders IP
    if ip == game.player2.getIP():
        ip = game.player1.getIP()  # get the ip address
    else:
        # reverse the move to the second client who is waiting for his turn
        old_rect_num = get_reverse_rect_number(str(old_rect_num))  # reverse
        new_rect_num = get_reverse_rect_number(str(new_rect_num))  # reverse
        ip = game.player2.getIP()  # get the ip address
    return ip, old_rect_num, new_rect_num


def check_movable_cards_not_over(ip, game: Game):
    """
    check if the movable cards are not over for a client because if
    they are, he lose in the game
    :param ip: the ip address
    :param game: the game object
    :return: boolean answer
    """
    flag = False
    for value in game.board_dict.values():
        if value is not None:
            if value[1] == ip and value[0] not in ["11", "12"]:
                flag = True
                break
    return flag


def turn_is_legal(distance, old_rect_num, new_rect_num):
    """
    check if a tun is legal by the distance
    :param distance: the distance between the rectangles
    :param old_rect_num: the source rect number
    :param new_rect_num: the destination rect number
    :return: boolean answer (true / false)
    """
    return distance == 10 or (distance == 1 and str(old_rect_num)[0] == str(new_rect_num)[0]) \
           or (old_rect_num // 10 == 0 and new_rect_num // 10 == 0)


def send_win_lose(game: Game, ip, game_comm):
    """
    send to the clients if they win or lose:
    :param game: the game object
    :param ip: the ip address of the sender of the turn
    :param game_comm: the game communication
    :return: None
    """
    games.games_list.remove(game)
    games.amount_of_games -= 1
    games.amount_of_users -= 2

    game_comm.send_specific_client("11L", ip)

    ip = get_second_client_ip(ip, game)

    game_comm.send_specific_client("11W", ip)


# command number 2
def handleTurn(data, ip, game: Game, game_comm):
    """
    handle a turn by the action that a player made
    return to the 2 players what to do by handling the turn
    :param data: the old and new rect numbers to move a card
    :param ip: the ip address of the one who made the turn
    :param game: the game object
    :param game_comm: the communication obj of the game
    :return: None
    """
    old_rect_num, new_rect_num = data.split()  # split the data to save the old and new rectangles numbers
    old_rect_num, new_rect_num = int(old_rect_num), int(new_rect_num)  # change the type of them to integers

    # save the original locations that in charge about what the clients will see
    old_rect_num_at_client = old_rect_num  # save the old rect location
    new_rect_num_at_client = new_rect_num  # save the new rect location

    data = str(old_rect_num) + " " + str(new_rect_num) + " "  # create the data to return

    # if the user is user number 2 (the reversed user),
    # reverse the move at the server (reverse the locations art the server):

    if ip == game.player2.getIP():
        # reverse the move
        old_rect_num = get_reverse_rect_number(str(old_rect_num))  # reverse
        new_rect_num = get_reverse_rect_number(str(new_rect_num))  # revers
        print("old - ", old_rect_num)
        print("new - ", new_rect_num)
    distance = abs(old_rect_num - new_rect_num)  # create the distance variable to check if the move is legal

    # if the move is correct, send to the both clients the updates to make:
    if turn_is_legal(distance, old_rect_num, new_rect_num):

        # after we checked if the move is legal, check if there isn't a fight or if there is:

        # if the new rect is free, move the card to this rect
        # there isn't a fight:

        if game.board_dict[new_rect_num] is None:

            move(old_rect_num, new_rect_num, game)  # save the new places and delete the old
            print("\n", game.board_dict, "\n")
            print("move card to new place, regular move")

            # send the data to the client that made his turn
            dst_card_level = 13  # that means that there isn't a fight, just a regular move (there is no card 13)
            data = "02" + data + str(dst_card_level)  # create the data to send
            game_comm.send_specific_client(data, ip)  # send the data to the client who made his turn

            # check who is the second client to send the data to him by comparing the senders IP
            # and reverse the data if there is a need to get the locations of the enemy (old and new rectangles numbers)
            ip, enemy_old_rect_num, enemy_new_rect_num = \
                get_waiting_client_ip_and_update_rectangles(ip, game, old_rect_num, new_rect_num)

            # create the data and send the enemy locations
            data = "03" + str(enemy_old_rect_num) + " " + str(enemy_new_rect_num)  # create the data to return
            game_comm.send_specific_client(data, ip)  # send the update to the second player

        # if the new rect is taken, do a fight:
        else:
            global ip2
            # check who should win the fight
            src_card_level = int(game.board_dict[old_rect_num][0])  # the level of the source card
            dst_card_level = int(game.board_dict[new_rect_num][0])  # the level of the destination card

            # if flag found:
            if dst_card_level == 12:
                games.games_list.remove(game)
                games.amount_of_games -= 1
                games.amount_of_users -= 2

                # send the turn to the client who made his turn and
                # send him the enemy card number to show before moving (the destination card)
                data = "09" + data + str(dst_card_level)
                game_comm.send_specific_client(data, ip)  # send the data to the client who made his turn

                # check who is the second client to send the data to him by comparing the senders IP
                # and reverse the data if there is a need to get the locations of the enemy(old and
                # new rectangles numbers).
                # the client who will get the data will show the enemy card and then will
                # move the enemy card on his card and delete his card from the game
                ip2, old_rect_num_at_client, new_rect_num_at_client = \
                    get_waiting_client_ip_and_update_rectangles(ip, game, old_rect_num, new_rect_num)

                # create the data and send
                data = "10" + str(old_rect_num_at_client) \
                       + " " + str(new_rect_num_at_client) + " " + str(src_card_level)
                game_comm.send_specific_client(data, ip2)  # send the update to the second player

            # if the source card wins:
            elif src_card_level > dst_card_level and not (src_card_level == 10 and dst_card_level == 1) \
                    or (src_card_level == 3 and dst_card_level == 11) \
                    or (src_card_level == 1 and dst_card_level == 10):

                move(old_rect_num, new_rect_num, game)  # save the new places and delete the old

                # send the turn to the client who made his turn and
                # send him the enemy card number to show before moving (the destination card)
                data = "02" + data + str(dst_card_level)
                game_comm.send_specific_client(data, ip)  # send the data to the client who made his turn

                # check who is the second client to send the data to him by comparing the senders IP
                # and reverse the data if there is a need to get the locations of the enemy(old and
                # new rectangles numbers).
                # the client who will get the data will show the enemy card and then will
                # move the enemy card on his card and delete his card from the game
                ip2, old_rect_num_at_client, new_rect_num_at_client = \
                    get_waiting_client_ip_and_update_rectangles(ip, game, old_rect_num, new_rect_num)

                # create the data and send
                data = "04" + str(old_rect_num_at_client) \
                       + " " + str(new_rect_num_at_client) + " " + str(src_card_level)
                game_comm.send_specific_client(data, ip2)  # send the update to the second player

            # if the destination card wins:
            elif src_card_level < dst_card_level and not (src_card_level == 1 and dst_card_level == 10) \
                    or (src_card_level == 11 and dst_card_level == 3) \
                    or (src_card_level == 10 and dst_card_level == 1):

                game.board_dict[old_rect_num] = None  # delete the source card from the game

                # send the data to the client that did his turn
                # that he needs to remove his card from the game and to show the enemy's card
                data = "05" + str(old_rect_num_at_client) + " " + str(new_rect_num_at_client) + " " + str(
                    dst_card_level)
                game_comm.send_specific_client(data, ip)  # send the data to the client who made his turn

                # check who is the client to send to the data by checking and comparing the senders IP
                # and reverse the location numbers values if there is a need to
                ip2, old_rect_num_at_client, new_rect_num_at_client = \
                    get_waiting_client_ip_and_update_rectangles(ip, game, old_rect_num, new_rect_num)

                # send the data to the second client
                data = "06" + str(old_rect_num_at_client) + " " + str(new_rect_num_at_client) + " " + str(
                    src_card_level)
                game_comm.send_specific_client(data, ip2)  # send the data to the client who made his turn

            # if the cards are even, delete them both
            else:
                game.board_dict[old_rect_num] = None  # delete card from the game
                game.board_dict[new_rect_num] = None  # delete card from the game

                # send the data to the client who made his turn, because there is a tie,
                # the client will need to show the enemy's card and than delete both cards from the game
                data = "07" + str(old_rect_num_at_client) + " " + str(new_rect_num_at_client) + " " + str(
                    dst_card_level)
                game_comm.send_specific_client(data, ip)

                # check who is the client to send to the data by checking and comparing the senders IP
                # and reverse the location numbers values if there is a need to
                ip2, old_rect_num_at_client, new_rect_num_at_client = \
                    get_waiting_client_ip_and_update_rectangles(ip, game, old_rect_num, new_rect_num)

                # send the data to the second user that is waiting for his turn send him to show the enemy's card and to
                # delete both cards from the game
                data = "08" + str(old_rect_num_at_client) + " " + str(new_rect_num_at_client) + " " + str(
                    src_card_level)
                game_comm.send_specific_client(data, ip2)

            # check if one of the clients don't have cards to move
            # if that's the case, end the game with a winner and a loser
            if not check_movable_cards_not_over(ip, game):
                send_win_lose(game, ip, game_comm)

            elif not check_movable_cards_not_over(ip2, game):
                send_win_lose(game, ip2, game_comm)

    else:
        # if the turn is wrong, send back to the client that he needs to try again
        data = f"f{old_rect_num_at_client}"
        data = "02" + data
        # send the data to the client that did his turn
        game_comm.send_specific_client(data, ip)


# handle messages for the main server:
threading.Thread(target=handle_msgs, args=(comm, recv_q, None), daemon=True).start()
