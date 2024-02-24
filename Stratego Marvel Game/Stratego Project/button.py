import pygame
from pygame.locals import *


class Button:

    def __init__(self, x, y, text, width, height, text_col, button_col, hover_col):
        """
        constructor:
        :param x: the x location
        :param y: the y location
        :param text: the text to print on the button
        :param width: the width of the button
        :param height: the height of the button
        :param text_col: the text color
        :param button_col: the button color
        :param hover_col: the color when we cover the button after it got pressed
        """
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.text_col = text_col
        self.button_col = button_col
        self.hover_col = hover_col
        self.font = pygame.font.SysFont('Constantia', 30)  # the font
        self.button_rect = Rect(self.x, self.y, self.width, self.height)  # create pygame Rect object for the button

    def draw_button(self, screen, pressed):
        """
        draw the button by the given arguments
        :param screen: the screen of the game
        :param pressed: if the button pressed or not
        :return: None
        print the button differently if it pressed or not
        """
        if not pressed:
            # create pygame Rect object for the button
            pygame.draw.rect(screen, self.button_col, self.button_rect)
        else:
            # create pygame Rect object for the button
            pygame.draw.rect(screen, self.hover_col, self.button_rect)
        self._add_txt_to_button(screen)  # add the text to the button

    def _add_txt_to_button(self, screen):
        """
        add the text to the button
        :param screen: the game screen
        :return: None
        """
        # add text to button
        text_img = self.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        print("pressed")

    def is_button_pressed(self, mouse_pos, screen):
        """
        check if the current button got pressed
        :param mouse_pos: the position of the mouse
        :param screen: the game screen
        :return: boolean answer if the button pressed or not
        """
        flag = False  # the answer
        x, y = mouse_pos
        if self.button_rect.collidepoint(x, y):  # check if the current button pressed
            flag = True  # set the flag to True because the button pressed
            self.draw_button(screen, True)  # draw the pressed button
        return flag

    def _draw_pressed_button(self, screen):
        """
        draw the button
        :param screen: the game screen
        :return: None
        """
        # create pygame Rect object for the button
        pygame.draw.rect(screen, self.hover_col, self.button_rect)
