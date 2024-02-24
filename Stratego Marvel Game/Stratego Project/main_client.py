import pygame
import sys
import queue
from button import Button
from cards import Card
from board_rectangles import BoardRectangle
import threading
from client_com import ClientComm
from enemy import Enemy


# define the RGB values for the colors:
WHITE = (255, 255, 255)  # white
BLACK = (0, 0, 0)  # black
YELLOW = (255, 255, 0)  # yellow
LIME = (0, 255, 0)  # lime
color_light = (170, 170, 170)  # light shade of the button
color_dark = (100, 100, 100)  # dark shade of the button
BLUE2 = (70, 159, 237)  # blue
BLUE = (30, 144, 255)  # blue
RED = (227, 2, 41)  # red
RED2 = (255, 0, 0)  # red
GREEN = (34, 139, 34)  # green

# load the screens
open_screen = pygame.image.load("screens_client\start_screen.jpg")  # the opening screen
nickname_screen = pygame.image.load("screens_client\input_nickname_screen.jpg")  # the input nickname screen
menu_screen = pygame.image.load("screens_client\menu_screen.PNG")  # the menu screen
building_screen = pygame.image.load("screens_client\\build_the_board_screen.jpg")  # the building the board screen
blue_cover = pygame.image.load("screens_client\\blue_cover.jpg")  # blue cover
waiting_screen = pygame.image.load("screens_client\waiting_for_player_screen.jpg")  # waiting screen
game_screen = pygame.image.load("screens_client\game_screen.jpg")  # game screen
win_screen = pygame.image.load("screens_client\win_screen.jpg")  # win screen
lose_screen = pygame.image.load("screens_client\lose_screen.jpg")  # lose screen
instructions_screen = pygame.image.load("screens_client\instructions.jpg")  # instructions screen
story_screen = pygame.image.load("screens_client\story.jpg")  # background story screen


# load the cards images
card1_img = pygame.image.load("screens_client\card1.jpg")
card2_img = pygame.image.load("screens_client\card2.jpg")
card3_img = pygame.image.load("screens_client\card3.jpg")
card4_img = pygame.image.load("screens_client\card4.jpg")
card5_img = pygame.image.load("screens_client\card5.jpg")
card6_img = pygame.image.load("screens_client\card6.jpg")
card7_img = pygame.image.load("screens_client\card7.jpg")
card8_img = pygame.image.load("screens_client\card8.jpg")
card9_img = pygame.image.load("screens_client\card9.jpg")
card10_img = pygame.image.load("screens_client\card10.jpg")
bomb_img = pygame.image.load("screens_client\\bomb.jpg")
infinity_glove_img = pygame.image.load("screens_client\infinity_glove.jpg")

# create the cards:
card1_1 = Card("Wonda", card1_img, (875, 250), 1, None, None)

card2_1 = Card("Deadpool", card2_img, (875, 300), 2, None, None)
card2_2 = Card("Deadpool", card2_img, (875, 350), 2, None, None)
card2_3 = Card("Deadpool", card2_img, (875, 400), 2, None, None)
card2_4 = Card("Deadpool", card2_img, (875, 450), 2, None, None)
card2_5 = Card("Deadpool", card2_img, (875, 500), 2, None, None)
card2_6 = Card("Deadpool", card2_img, (875, 550), 2, None, None)
card2_7 = Card("Deadpool", card2_img, (875, 600), 2, None, None)
card2_8 = Card("Deadpool", card2_img, (875, 650), 2, None, None)

card3_1 = Card("Black panther", card3_img, (950, 250), 3, None, None)
card3_2 = Card("Black panther", card3_img, (950, 300), 3, None, None)
card3_3 = Card("Black panther", card3_img, (950, 350), 3, None, None)
card3_4 = Card("Black panther", card3_img, (950, 400), 3, None, None)
card3_5 = Card("Black panther", card3_img, (950, 450), 3, None, None)

card4_1 = Card("Wolverine", card4_img, (950, 500), 4, None, None)
card4_2 = Card("Wolverine", card4_img, (950, 550), 4, None, None)
card4_3 = Card("Wolverine", card4_img, (950, 600), 4, None, None)
card4_4 = Card("Wolverine", card4_img, (950, 650), 4, None, None)

card5_1 = Card("Spiderman", card5_img, (1025, 250), 5, None, None)
card5_2 = Card("Spiderman", card5_img, (1025, 300), 5, None, None)
card5_3 = Card("Spiderman", card5_img, (1025, 350), 5, None, None)
card5_4 = Card("Spiderman", card5_img, (1025, 400), 5, None, None)

card6_1 = Card("Thor", card6_img, (1025, 450), 6, None, None)
card6_2 = Card("Thor", card6_img, (1025, 500), 6, None, None)
card6_3 = Card("Thor", card6_img, (1025, 550), 6, None, None)
card6_4 = Card("Thor", card6_img, (1025, 600), 6, None, None)

card7_1 = Card("Hulk", card7_img, (1025, 650), 7, None, None)
card7_2 = Card("Hulk", card7_img, (1100, 250), 7, None, None)
card7_3 = Card("Hulk", card7_img, (1100, 300), 7, None, None)

card8_1 = Card("Dr.Strange", card8_img, (1100, 350), 8, None, None)
card8_2 = Card("Dr.Strange", card8_img, (1100, 400), 8, None, None)

card9_1 = Card("Caption America", card9_img, (1100, 450), 9, None, None)

card10_1 = Card("Iron Man", card10_img, (1100, 500), 10, None, None)

card_bomb_1 = Card("bomb", bomb_img, (1100, 550), 11, None, None)
card_bomb_2 = Card("bomb", bomb_img, (1100, 600), 11, None, None)
card_bomb_3 = Card("bomb", bomb_img, (1100, 650), 11, None, None)
card_bomb_4 = Card("bomb", bomb_img, (1175, 250), 11, None, None)
card_bomb_5 = Card("bomb", bomb_img, (1175, 300), 11, None, None)
card_bomb_6 = Card("bomb", bomb_img, (1175, 350), 11, None, None)

card_infinity_glove = Card("infinity_glove", infinity_glove_img, (1175, 400), 12, None, None)

# put the cards in a cards list:
cards_list = [card1_1, card2_1, card2_2, card2_3, card2_4, card2_5, card2_6, card2_7, card2_8, card3_1, card3_2,
              card3_3, card3_4, card3_5, card4_1, card4_2, card4_3, card4_4, card5_1, card5_2, card5_3, card5_4,
              card6_1, card6_2, card6_3, card6_4, card7_1, card7_2, card7_3, card8_1, card8_2, card9_1, card10_1,
              card_bomb_1, card_bomb_2, card_bomb_3, card_bomb_4, card_bomb_5, card_bomb_6, card_infinity_glove]

board_rectangles_list = []  # a list of all the rectangles of the board game (100 rect)

enemy_rect = Enemy(BLUE, None)  # an object of enemy that has the enemy's hide color

last_pos = None  # saves the last position that the user pressed in the game
turn = False  # a flag that represents a turn in the game
cards_color = YELLOW  # cards color, will change by the server

nickname = "player"  # nickname
other_player_nickname = "other player"  # other player nickname

# a dict with the cards images and the levels of the cards (level: image)
cards_img_dict = {1: card1_img,
                  2: card2_img,
                  3: card3_img,
                  4: card4_img,
                  5: card5_img,
                  6: card6_img,
                  7: card7_img,
                  8: card8_img,
                  9: card9_img,
                  10: card10_img,
                  11: bomb_img,
                  12: infinity_glove_img}

run = True  # flag that represents when we need to close the game

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# assigning values to X and Y variable
width_screen = 1459
height_screen = 824

# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode((width_screen, height_screen))

# set the pygame window name
pygame.display.set_caption('STRATEGO marvel')


def open_screen_def(start_button):
    """
    this def shows the opening screen of the game until the user press on the start button
    :param start_button: a button
    :return: None
    """
    # print the opening screen
    screen.blit(open_screen, (0, 0))  # print the opening screen
    start_button_pressed = False  # a flag that represents if the button pressed
    start_button.draw_button(screen, False)  # print the "start button"

    while True:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if the user pressed 'start' and the button is up, move to the next screen
            if start_button_pressed and event.type == pygame.MOUSEBUTTONUP:
                return
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # check if the user pressed on the mouse:
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_pos = pygame.mouse.get_pos()  # get the position of the pressed mouse
                # check if the user pressed on one of the buttons:
                start_button_pressed = start_button.is_button_pressed(mouse_pos, screen)
            # Draws the surface object to the screen.
            pygame.display.update()


def nickname_input_screen_def():
    """
    show the nickname screen and return after the user typed
    his nickname and pressed enter
    :return: the user nickname
    """
    # print the opening screen
    screen.blit(nickname_screen, (0, 0))  # print the opening screen
    # create the input rectangle
    input_rect = pygame.Rect(600, 600, 280, 50)  # the rect with the input
    zero_input_rect = pygame.Rect(600, 600, 280, 50)  # the rect without the input

    user_text = ""  # the nickname to return
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)

    while True:

        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # backspace
                elif event.key == pygame.K_RETURN and len(user_text) > 0:
                    return user_text
                # Unicode standard is used for string
                # formation
                else:
                    if len(user_text) < 15:  # check the length of the nickname
                        user_text += event.unicode

        if len(user_text) == 0:
            pygame.draw.rect(screen, WHITE, zero_input_rect)  # color_passive
            text_surface = base_font.render("Please enter a nickname", True, BLUE2)
            # render at position stated in arguments
            screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
        else:
            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(screen, WHITE, input_rect)
            text_surface = base_font.render(user_text, True, RED2)

            # render at position stated in arguments
            screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
        pygame.display.update()


def menu_screen_def(play_button, instructions_button, back_button):
    """
    print the menu screen and action by the user's mouse pressings
    :param play_button: the button to start a game
    :param instructions_button: the button who leads to the instructions
    :param back_button: the button who leads back to menu
    :return: None (get back from the def when the user selected 'play')
    """
    # init menu screen variables and set the screen up:
    play_button_pressed, instructions_button_pressed = set_menu(play_button, instructions_button)

    while True:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # check if the user pressed on the mouse:
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_pos = pygame.mouse.get_pos()  # get the position of the pressed mouse
                # check if the user pressed on one of the buttons:
                play_button_pressed = play_button.is_button_pressed(mouse_pos, screen)
                instructions_button_pressed = instructions_button.is_button_pressed(mouse_pos, screen)
            else:
                if play_button_pressed:  # if the play button pressed
                    play_button.draw_button(screen, False)  # print the "play button"
                    if event.type == pygame.MOUSEBUTTONUP:
                        return

                elif instructions_button_pressed:  # if the instruction button pressed
                    instructions_button.draw_button(screen, False)  # print the "instructions screen"
                    instructions(back_button)  # show the instructions
                    # init menu screen variables and set the screen up:
                    play_button_pressed, instructions_button_pressed = set_menu(play_button, instructions_button)
            # Draws the surface object to the screen.
            pygame.display.update()


def set_menu(play_button, instructions_button):
    """
    print th screen, the buttons, and init the buttons objects,
    and print welcome to the user by his nickname
    :param play_button:
    :param instructions_button:
    :return: inited play_button_pressed and instructions_button_pressed (false variables)
    """
    screen.blit(menu_screen, (0, 0))  # print the menu screen

    # print the home screen
    screen.blit(menu_screen, (0, 0))  # print the menu screen
    play_button_pressed = False
    play_button.draw_button(screen, False)  # print the "play button"
    instructions_button_pressed = False
    instructions_button.draw_button(screen, False)  # print the "instructions screen"

    base_font = pygame.font.Font(None, 32)  # the font
    text_surface = base_font.render("welcome " + nickname, True, BLUE2)
    # render at position stated in arguments
    screen.blit(text_surface, (20, 20))  # print the text on the screen

    return play_button_pressed, instructions_button_pressed


def instructions(back_button):
    """
    show the instructions
    :param back_button: if the button pressed on the back button, return
    :return: None
    """
    screen.blit(instructions_screen, (0, 0))  # print the instructions screen
    back_button.draw_button(screen, False)  # print the "back button"
    back_button_pressed = False
    while True:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # check if the user pressed on the mouse:
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_pos = pygame.mouse.get_pos()  # get the position of the pressed mouse
                back_button_pressed = back_button.is_button_pressed(mouse_pos, screen)
            elif back_button_pressed:
                back_button_pressed = False
                back_button.draw_button(screen, False)  # print the "instructions screen"
                if event.type == pygame.MOUSEBUTTONUP:
                    return
            # Draws the surface object to the screen.
            pygame.display.update()


def background_story(next_button):
    """
    show the background story on the screen before the game
    :param next_button: if the user pressed on the 'next' button, return
    :return: None
    """
    screen.blit(story_screen, (0, 0))  # print the menu screen
    next_button.draw_button(screen, False)
    next_button_pressed = False
    while True:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # check if the user pressed on the mouse:
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_pos = pygame.mouse.get_pos()  # get the position of the pressed mouse
                next_button_pressed = next_button.is_button_pressed(mouse_pos, screen)
            # if the next button pressed:
            elif next_button_pressed:
                next_button_pressed = False
                next_button.draw_button(screen, False)
                # if the mouse button is up after the user pressed on it, return
                if event.type == pygame.MOUSEBUTTONUP:
                    return

            # Draws the surface object to the screen.
            pygame.display.update()


def draw_board_rectangles():
    """
    draw the game board's 100 rectangles and save
    the inited objects in the list board_rectangles_list
    :return: None
    """
    # draw the board (100 board's rectangles):
    # run on the y line
    for y in range(10):
        # run on the x line
        for x in range(10):
            rect = pygame.Rect((105 + x * 105 - x * 34, 57 + y * 57 + y * 14, 70, 70))  # create the card_rect variables
            rect_color = GREEN
            if y % 2 == 0:
                if x % 2 == 0:
                    rect_color = BLACK
            else:
                if not(x % 2 == 0):
                    rect_color = BLACK
            # add the card_rect to the boards rectangles list
            board_rectangles_list.append(BoardRectangle(rect, rect_color, None, y * 10 + x))
            pygame.draw.rect(screen, rect_color, rect)  # draw the rect on the screen


def build_the_game_board():
    """
    print the game board's screen and the cards on the right side,
    the user will need to build his game board side
    :return: None
    """
    # print the building_screen
    screen.blit(building_screen, (0, 0))  # print the building_screen

    # draw the board's rectangles:
    draw_board_rectangles()

    set_cards_on_screen()  # set the cards on the screen
    pressed_card = None
    global last_pos
    amount_cards_on_board = 0
    while True:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            # if the user pressed on the screen:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the user pressed on one of the cards
                mouse_pos = pygame.mouse.get_pos()  # get the position of the mouse
                # check if a board card_rect pressed, get card_rect obj or None
                board_rect_obj = check_board_rect_pressed(mouse_pos)

                # if the user didn't select a card yet, check if the user selected:
                if last_pos is None:
                    # check if a card pressed, get the card or None
                    pressed_card = check_card_pressed(mouse_pos)
                    # if the user pressed on a card
                    if pressed_card is not None:
                        # if the user selected a card that is on the board to move:
                        select_card(pressed_card, LIME)
                        last_pos = pressed_card.getPos()
                        print("\nselected a card\n")

                else:
                    # if the user pressed on a card_rect to put the card on and the card_rect is in the range:
                    if board_rect_obj is not None and mouse_pos[1] > 500:

                        # check if the user selected to put a card on a card (on a taken card_rect):
                        if board_rect_obj.getCard() is not None:
                            print("this card_rect has a card on")
                        # the user selected to put the card on an empty card_rect, put the card there
                        else:
                            # if the position of the pressed card isn't on the board, print the blue background
                            if check_board_rect_pressed(last_pos) is None:
                                amount_cards_on_board += 1
                                print(f'amount of cards on board: {amount_cards_on_board}')
                                screen.blit(blue_cover, last_pos)

                            else:
                                # draw a cover by the the rect color and the card on it
                                draw_card_rect_cover(pressed_card)

                            move_card_new_place(pressed_card, board_rect_obj)
                            last_pos = None  # init the user's choice
                    else:
                        # if a card pressed again and the board didn't get pressed
                        # init the user's choice
                        if pressed_card is not None:
                            draw_init_choice(pressed_card)  # draw the card back with it's original rect color
                            last_pos = None  # init the user's choice
        pygame.display.update()
        # if the user put all the cards on the board:
        if amount_cards_on_board == 40:
            return


def draw_card_rect_cover(card):
    """
    cover the card by the card's rect
    :param card: card object
    :return: None
    """
    card_rect = card.getCard_rect()  # get the rect of the card
    card_rect.width += 2
    card_rect.height += 2
    pygame.draw.rect(screen, card.getCard_rect_color(), card_rect)


def move_card_new_place(card, dst_rect):
    """
    print the card in the new rectangle
    :param card: card object
    :param dst_rect: destination rect object
    :return: None
    """
    src_rect = card.getRect()  # get the last rect before the moving

    card.setPos((dst_rect.getRect().x + 5, dst_rect.getRect().y + 10))  # change the cards position
    # put the card in the new place
    card_rect = card.getCard_rect()
    card_rect.x, card_rect.y = card.getPos()  # set the x and y positions
    screen.blit(card.getImg(), card_rect)

    pygame.draw.rect(screen, cards_color, card_rect, 2)
    card.setRect(dst_rect)  # set the rect in the cards object
    dst_rect.setCard(card)  # set the card in the rect object
    card.setCard_rect_color(dst_rect.getColor())
    print(f"new place for {card.getName()}")

    # delete the card from the last rectangle object memory
    if src_rect is not None:
        src_rect.setCard(None)  # delete the card from the source rect


def print_rect_taken_by(rect):
    """
    print if the current rectangle has a card on or not.
    if it has, print the cards name
    :param rect: a board rectangle object
    :return: None
    """
    rect_card = rect.getCard()  # get the rect object card
    if rect_card is not None:
        print(f"card_rect taken by: {rect_card.getName()}")
        pass
    else:
        print("this card_rect is empty")


def check_board_rect_pressed(mouse_pos):
    """
    check if a rectangle of the board pressed
    :param mouse_pos: the mouse position
    :return: the board rectangle object that pressed or None
    """
    rect_obj = None  # the value to return
    for board_rect in board_rectangles_list:
        if board_rect.getRect().collidepoint(mouse_pos):  # if the user pressed on the card_rect
            rect_obj = board_rect
            print_rect_taken_by(rect_obj)  # print card_rect situation
            break
    return rect_obj


def set_cards_on_screen():
    """
    set the cards on the screen
    :return: None
    """
    for card in cards_list:
        set_card_on_screen(card)


def set_card_on_screen(card):
    """
    print the card on the screen
    :param card: a card object
    :return:
    """
    img = card.getImg()  # get the image of the card
    img.convert()
    rect = card.getCard_rect()
    rect.x, rect.y = card.getPos()  # set the rect position
    screen.blit(img, rect)  # print the card
    pygame.draw.rect(screen, cards_color, rect, 2)  # print the card_rect


def check_card_pressed(mouse_pos):
    """
    check if a card pressed
    :param mouse_pos:
    :return: the card object or None
    """
    ret = None  # the card object to return
    for card in cards_list:
        rect = card.getCard_rect()
        if rect.collidepoint(mouse_pos):  # if the card pressed
            ret = card
            print(f"pressed on {str(ret.getName())}")
            break
    return ret


def create_sending_starting_board():
    """
    create the data to send to the server that conclude
    the command number '01', the nickname of the user and
    the game board (string with a rect numbers and cards numbers)
    :return: return the string to send to the server
    """
    board_msg = "01" + str(len(nickname)).zfill(2) + str(nickname)  # set the command number first in the message
    for rect_num in range(60, 100):
        card = board_rectangles_list[rect_num].getCard()  # get the card  of the rectangle
        if card is not None:
            card_num = card.getLevel()  # get the level of the card that is on the card_rect
            board_msg += str(rect_num) + "$" + str(card_num) + "@"  # add to the message
    return str(len(board_msg)).zfill(3) + board_msg[:-1]


def connect_to_server():
    """
    connect to the server
    :return: a queue recv_q and the connection comm
    """
    recv_q = queue.Queue()  # create the queue
    comm = ClientComm('192.168.0.117', 1000, recv_q)  # create the connection between the client and the server
    print("connected to the server")
    return recv_q, comm


def set_enemies_on_screen():
    """
    print the enemies on the screen
    :return: None
    """
    # loop over all the first 40 rectangles on screen
    for rect in range(40):
        board_rect_x, board_rect_y = board_rectangles_list[rect].getRect().x, board_rectangles_list[rect].getRect().y
        enemy_rect.setPos((board_rect_x + 5, board_rect_y + 10))
        rect_of_enemy = enemy_rect.getRect()

        if cards_color == BLUE:
            enemy_rect_color = RED
        else:
            enemy_rect_color = BLUE

        pygame.draw.rect(screen, enemy_rect_color, rect_of_enemy)
        pygame.draw.rect(screen, WHITE, rect_of_enemy, 2)


def connect_to_game(leave_game_button):
    """
    connect to the server and wait for another client to join the game
    :param leave_game_button: if the user will select to press that button, the program will close
    :return: None
    """

    screen.blit(waiting_screen, (0, 0))  # print the waiting_screen
    pygame.display.update()  # update

    recv_q, comm = connect_to_server()  # connection

    thread = threading.Thread(target=handle_msgs, args=(recv_q,), daemon=True)  # get information from the server
    thread.start()  # start the thread
    # send the game board to the server:
    # create the game board data to send to the server that conclude the nickname
    # and the game boards
    board_msg = create_sending_starting_board()
    comm.send(board_msg)  # try to send to the server
    print("sent to the server")

    while True:

        # if the run flag is off, close the program
        if not run:
            # deactivates the pygame library
            pygame.quit()
            # quit the program.
            quit()

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()

        # when we will get info from the server we
        # will change the cards color and than we will start the game
        if cards_color is not YELLOW:
            game_events(comm, leave_game_button)
            break


def game_events(comm, leave_game_button):
    """
    game loop
    :param comm: the communication
    :param leave_game_button: leave the game if the user pressed on it
    :return:
    """
    pressed_card = None  # a global variable that has the last card that the user pressed on or None
    global last_pos  # a global variable that has the last position of the card that the user pressed or None
    global turn  # a flag of the turn
    global nickname  # the user's nickname
    global other_player_nickname # the other user's nickname

    # print the home screen
    screen.blit(game_screen, (0, 0))  # print the building_screen

    # draw the board's rectangles:
    draw_board_rectangles()

    set_cards_on_screen()  # set the cards on the screen

    set_enemies_on_screen()  # set the enemies card on the screen

    leave_game_button.draw_button(screen, False)  # print the "leave_game_button"

    pygame.display.update()  # update

    while True:

        if not run:
            # deactivates the pygame library
            pygame.quit()
            # quit the program.
            quit()

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both:
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()

            # if the user pressed on the screen:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the user pressed on one of the cards
                mouse_pos = pygame.mouse.get_pos()  # get the position of the mouse

                if leave_game_button.is_button_pressed(mouse_pos, screen):
                    command_number11("l")

                # if that the user's turn in the game
                if turn:

                    # check if a board card_rect pressed, get card_rect obj or None
                    board_rect_obj = check_board_rect_pressed(mouse_pos)

                    # if the user didn't select a card yet, check if the user selected:
                    if last_pos is None:
                        # check if a card pressed, get the card or None
                        pressed_card = check_card_pressed(mouse_pos)

                        # if the user pressed on a card and the card is legal to move
                        if pressed_card is not None and pressed_card.getLevel() not in [11, 12]:
                            # if the user selected a card that is on the board to move:
                            select_card(pressed_card, LIME)  # print the card rect in another color
                            last_pos = pressed_card.getPos()

                    else:
                        # if the user pressed on a card_rect to put the card on and the card_rect is in the range:
                        if board_rect_obj is not None:

                            # check if the user selected to put a card on a card (on a taken card_rect):
                            if board_rect_obj.getCard() is not None:
                                print("this card_rect has a card on")
                            # the user selected to put the card on an empty card_rect, put the card there
                            else:

                                # send to the server and get permission
                                # to move the card:

                                # get the old and new rects numbers
                                old_rect_num, new_rect_num = getRectanglesNumbers(pressed_card, board_rect_obj)
                                userTurnToServer(old_rect_num, new_rect_num, comm)  # sent the turn to the server
                                # draw_card_rect_cover(pressed_card)
                                # move_card_new_place(pressed_card, board_rect_obj)
                                last_pos = None
                                turn = False  # the turn moves to the second player
                        else:
                            # if a card pressed again and the board didn't get pressed
                            # init the user's choice (just draw the regular cards card_rect and init the choice)
                            if pressed_card is not None:
                                draw_init_choice(pressed_card)
                                last_pos = None
        pygame.display.update()


def getRectanglesNumbers(pressed_card, board_rect_obj):
    """
    get the old and new rectangles numbers
    :param pressed_card: the pressed card obj
    :param board_rect_obj: the boar object to move the card to
    :return: the old and new rectangles numbers
    """
    old_rect_num = pressed_card.getRect().getRect_num()  # get the number of the source rect
    new_rect_num = board_rect_obj.getRect_num()  # get number ofm the destination rectangle
    return old_rect_num, new_rect_num  # return


def userTurnToServer(old_rect_num, new_rect_num, comm):
    """
    sen the user's turn to the server
    :param old_rect_num: the number of the old rectangle of the card
    :param new_rect_num: the number of the new rectangle of the card
    :param comm: the communication object
    :return:
    """
    player_turn = "02" + str(old_rect_num) + " " + str(new_rect_num)
    comm.send(str(len(player_turn)).zfill(3) + player_turn)  # send the user's turn to the server


def select_card(pressed_card, rect_color):
    """
    draw the selected card rect in another color
    :param pressed_card: the card
    :param rect_color: the color of the card's rect
    :return: None
    """
    # if the user selected a card that is on the board to move:
    # select the card
    card_rect = pressed_card.getCard_rect()  # get the card's rect
    card_rect.x, card_rect.y = pressed_card.getPos()
    pygame.draw.rect(screen, rect_color, card_rect, 2)  # draw the rect


def move_card_turn(old_rect_num, new_rect_num):
    """
    move the card from the old rect number to the new rect number
    :param old_rect_num:
    :param new_rect_num:
    :return:
    """
    src_rect = board_rectangles_list[int(old_rect_num)]  # get the src rect
    print("src rect_num = ", src_rect.getRect_num())
    card = src_rect.getCard()  # get the card to move
    # if the card is exist:
    if card is not None:
        print("moving " + card.getName())
        dst_rect = board_rectangles_list[int(new_rect_num)]  # get the dst rect
        draw_card_rect_cover(card)  # draw the cover of the card
        move_card_new_place(card, dst_rect)  # move


def draw_init_choice(card):
    """
    draw the card's rect inited (by is's original color)
    :param card:
    :return:
    """
    card_rect = card.getCard_rect()  # get the rect card
    card_rect.x, card_rect.y = card.getPos()
    pygame.draw.rect(screen, cards_color, card_rect, 2)  # draw the rect


def handle_msgs(q):
    global run  # a flag if the program is running
    while True:
        data = q.get()  # get new data

        # if the data is exit, close and turn the run flag to false
        if data == "exit":
            print("exit")
            break

        handle_msg_by_command_number(data)  # handle messages by their command number
    run = False


def cover_enemy(rect_num):
    """
    cover enemy from the screen / delete enemy from the screen
    :param rect_num:
    :return:
    """
    # cover the old rectangle of the enemy:
    old_rect = board_rectangles_list[int(rect_num)]  # get the rectangle
    pygame.draw.rect(screen, old_rect.getColor(), old_rect)  # cover


def print_hidden_enemy(rect_num):
    """
    print the enemy that we will see his back and not the card itself
    :param rect_num: the rectangle number
    :return: None
    """
    # print the enemy in a new place:
    new_rect = board_rectangles_list[int(rect_num)]  # get the enemy's new rect
    # set the position of the enemy to the new rectangle
    enemy_rect.setPos((new_rect.getRect().x + 5, new_rect.getRect().y + 10))
    rect_of_enemy = enemy_rect.getRect()  # the enemy rect
    pygame.draw.rect(screen, enemy_rect.getColor(), rect_of_enemy)  # print on the screen the enemy in his new place
    pygame.draw.rect(screen, WHITE, rect_of_enemy, 2)


def print_enemy_in_new_place(old_rect_num, new_rect_num):
    """
    delete the enemy from it's old place and print it in the new place
    :param old_rect_num: the number of the current enemy's rect
    :param new_rect_num: the number of the rect to move the enemy to
    :return: None
    """
    cover_enemy(int(old_rect_num))
    print_hidden_enemy(new_rect_num)


def print_enemy_card_img(card_num, rect_num):
    """
    print the enemy's image card
    :param card_num: the number of the image to print
    :param rect_num: the rectangle number to print the picture at
    :return:
    """
    img = cards_img_dict[int(card_num)]  # get the image from the card image dict

    # print the enemy in a new place:
    new_rect = board_rectangles_list[int(rect_num)]  # get the enemy's new rect
    # set the position of the enemy to the new rectangle
    enemy_rect.setPos((new_rect.getRect().x + 5, new_rect.getRect().y + 10))
    rect_of_enemy = enemy_rect.getRect()  # the enemy rect
    screen.blit(img, rect_of_enemy)  # print the picture

    pygame.draw.rect(screen, enemy_rect.getColor(), rect_of_enemy, 2)
    pygame.time.wait(1000)  # wait a delay


def delete_card_from_game(rect_num):
    """
    delete a card from the game and from the screen
    :param rect_num: the rectangle number
    :return: None
    """
    # delete the card from the screen:
    old_rect = board_rectangles_list[int(rect_num)]  # get the rectangle
    pygame.draw.rect(screen, old_rect.getColor(), old_rect)  # cover

    # delete the card from the game
    card = old_rect.getCard()
    if card in cards_list:
        cards_list.remove(card)
    old_rect.setCard(None)  # delete the card from the rect


def command_number1(data):
    """
    connect to a game after getting info from the server
    select the color of the cards and for the enemies
    set if this is our turn or not
    :param data: the received data from the server
    :return: None
    """
    global cards_color  # the cards color
    global turn  # a boolean flag of the turn
    global other_player_nickname  # the nickname of the other player

    len_nickname = int(data[:2])  # get the len
    other_player_nickname = str(data[2:len_nickname + 2])  # get the other player's nickname
    player_number = str(data[2 + len(other_player_nickname):])  # get our player number

    print("len - " + str(len_nickname))
    print("other_player_nickname - " + other_player_nickname)
    print("data - " + data)

    # set the color of the card by the received data
    if player_number == "1":
        cards_color = BLUE
        enemy_rect.setColor(RED)
        turn = True
    elif player_number == "2":
        cards_color = RED
        enemy_rect.setColor(BLUE)


def command_number2(data):
    """
    move a card if the move is legal and if there is a fight, we win
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    global turn
    if not data.startswith("f"):
        # split the numbers of the rectangles (the src rect and the dst rect)
        old_rect_num, new_rect_num, card_num = data.split()  # split the data
        old_rect_num, new_rect_num, card_num = int(old_rect_num), int(new_rect_num), int(card_num)

        # if the server sent a enemy card num to show because there is a fight, show and win
        if int(card_num) is not 13:
            print_enemy_card_img(card_num, new_rect_num)  # show enemy's card

        # move our card
        move_card_turn(int(old_rect_num), int(new_rect_num))  # move the card
        pygame.display.update()  # update

    else:
        # the turn is illegal, init client's choice and give him to try again to make his turn
        print("\nillegal turn")
        card_rect_num = int(data[+1:])  # get the number of the rect of the card
        card = board_rectangles_list[card_rect_num].getCard()  # get the card
        draw_init_choice(card)  # draw the init choice
        turn = True


def command_number3(data):
    """
    move an enemy
    :param data: the data from the server that has the rectangles numbers
    :return: None
    """
    old_rect_num, new_rect_num = data.split()  # split the data
    print_enemy_in_new_place(old_rect_num, new_rect_num)  # print the enemy in new place
    print("printed enemy in new place!!!")


def command_number4(data):
    """
    if there is a fight during the other client's turn and the enemy's card wins,
    show the enemy and than move his card over our card and delete our card from the game
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    # show the enemy's card
    print_enemy_card_img(card_num, old_rect_num)

    print_enemy_in_new_place(old_rect_num, new_rect_num)  # print the enemy in a new place
    print("printed enemy in new place!!!")

    # delete the card from the game:
    cards_list.remove(board_rectangles_list[int(new_rect_num)].getCard())
    board_rectangles_list[int(new_rect_num)].setCard(None)  # delete the card from the rect


def command_number5(data):
    """
    there is a fight who made by our player and we lost, show the enemy and
    delete our player out from the game
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    # show the enemy's card and than after some seconds hide him
    print_enemy_card_img(card_num, new_rect_num)
    print_hidden_enemy(new_rect_num)

    delete_card_from_game(old_rect_num)  # delete our cad from the game


def command_number6(data):
    """
    the second player did his turn and lost in a fight
    show the enemy and delete it
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    # show the enemy card
    print_enemy_card_img(card_num, old_rect_num)

    # delete the enemy from the screen:
    old_rect = board_rectangles_list[int(old_rect_num)]  # get the rectangle
    pygame.draw.rect(screen, old_rect.getColor(), old_rect)  # cover


def command_number7(data):
    """
    # we did the turn and there is a tie, so show the enemy's card and
    delete the both cards
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    print_enemy_card_img(card_num, new_rect_num)  # print the enemy

    # cover the enemy:
    rect = board_rectangles_list[int(new_rect_num)]  # get the rectangle
    pygame.draw.rect(screen, rect.getColor(), rect)  # cover

    delete_card_from_game(old_rect_num)  # delete the card from the game


def command_number8(data):
    """
    the second user made his turn and there is a tie in the fight, show the enemy's card
    and delete both cards from the screen and from the game
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    print_enemy_card_img(card_num, old_rect_num)  # print the enemy

    # cover the enemy:
    rect = board_rectangles_list[int(old_rect_num)]  # get the rectangle
    pygame.draw.rect(screen, rect.getColor(), rect)  # cover

    delete_card_from_game(new_rect_num)  # delete the card from the game and from the screen


def command_number9(data):
    """
    winning by tacking the enemy's flag
    show the winning screen and close the program
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    global run  # the program run flag
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    print_enemy_card_img(card_num, new_rect_num)  # print the enemy's card

    move_card_turn(old_rect_num, new_rect_num)  # move the card

    screen.blit(win_screen, (0, 0))  # print the building_screen

    pygame.display.update()  # update screen
    pygame.time.wait(7000)  # wait
    run = False  # close the flag of the program


def command_number10(data):
    """
    losing by lose our flag (the another player got to our flag)
    :param data: the data from the server that has the rectangles numbers and the number of the card
    :return: None
    """
    global run
    old_rect_num, new_rect_num, card_num = data.split()  # split the data

    # show the enemy's card
    print_enemy_card_img(card_num, old_rect_num)

    print_enemy_in_new_place(old_rect_num, new_rect_num)  # print the enemy in a new place

    screen.blit(lose_screen, (0, 0))  # print the building_screen

    pygame.display.update()  # update screen
    pygame.time.wait(7000)  # wait
    run = False  # close the flag of the program


def command_number11(data):
    """
    win or lose by the server data
    :param data: the server msg - 'w' = win, another = lose
    :return: None
    """
    global run
    if data.lower() == "w":
        screen.blit(win_screen, (0, 0))  # print the building_screen
    else:
        screen.blit(lose_screen, (0, 0))  # print the building_screen

    pygame.display.update()  # update the screen
    pygame.time.wait(7000)  # wait
    run = False  # close the program's flag


def handle_msg_by_command_number(data):
    global last_pos  # the last position of the the pressed card
    global turn  # the turn flag
    global cards_color  # the color of the card
    global enemy_rect  # the enemy's rect obj
    global run  # the flag of the game's program

    command_number, data = int(data[:2]), str(data[2:])
    print("command_number " + str(command_number))

    # connect to a game
    if command_number == 1:
        command_number1(data)

    # regular move / fight we win
    if command_number == 2:
        command_number2(data)

    # enemy's move
    if command_number == 3:
        command_number3(data)
        turn = True

    # if there is a fight during the other client's turn and the enemy's card wins,
    # show the enemy and than move his card over our card and delete our card from the game
    if command_number == 4:
        command_number4(data)
        turn = True

    # there is a fight who made by our player and we lost, show the enemy and
    # delete our player out from the game
    if command_number == 5:
        command_number5(data)
        turn = False

    # the second player did his turn and lost in a fight
    # show the enemy and delete it
    if command_number == 6:
        command_number6(data)
        turn = True

    # we did the turn and there is a tie, so show the enemy's card and delete the both cards:
    if command_number == 7:
        command_number7(data)
        turn = False

    # the second user made his turn and there is a tie in the fight, show the enemy's card
    # and delete both cards from the screen and from the game:
    if command_number == 8:
        command_number8(data)
        turn = True

    # win by getting enemy's flag
    if command_number == 9:
        command_number9(data)

    # lose by losing our flag
    if command_number == 10:
        command_number10(data)

    # win or lose by the server data
    if command_number == 11:
        command_number11(data)

    last_pos = None  # init the last pos

    # print the game situation on the screen:
    base_font = pygame.font.Font(None, 32)
    pygame.draw.rect(screen, BLACK, (1000, 300, 400, 100))  # draw a black rect to cover
    if turn:
        # create the text surface and print it on the screen:

        text_surface = base_font.render("The turn is yours " + nickname, True, WHITE)
        # render at position stated in arguments
        screen.blit(text_surface, (1000, 300))

        text_surface = base_font.render("select a card to move!", True, RED)
        screen.blit(text_surface, (1000, 330))

    else:
        # create the text surface and print it on the screen:

        text_surface = base_font.render("That's " + other_player_nickname + "'s turn!", True, WHITE)
        # render at position stated in arguments
        screen.blit(text_surface, (1000, 300))

        text_surface = base_font.render("wait until the turn will be yours", True, WHITE)
        screen.blit(text_surface, (1000, 330))


def main():
    global nickname
    # create the buttons
    start_button = Button(640, 600, 'Start', 180, 70, BLACK, RED, color_dark)
    play_button = Button(75, 600, 'Play', 180, 70, BLACK, RED, color_dark)
    instructions_button = Button(75, 700, 'Instructions', 180, 70, BLACK, RED, color_dark)
    back_button = Button(640, 650, 'Back', 180, 70, BLACK, RED, color_dark)
    next_button = Button(640, 720, 'next', 180, 70, BLACK, RED, color_dark)
    leave_game_button = Button(1270, 730, 'leave and lose', 180, 70, WHITE, RED, color_dark)

    # print the start/open screen:
    open_screen_def(start_button)

    # print the input screen fo nickname
    nickname = nickname_input_screen_def()

    # print the menu screen:
    menu_screen_def(play_button, instructions_button, back_button)

    # show the background story before starting the game
    background_story(next_button)

    # print the "building the board" screen
    build_the_game_board()

    # create a connection between the client and the server
    connect_to_game(leave_game_button)


if __name__ == '__main__':
    main()
