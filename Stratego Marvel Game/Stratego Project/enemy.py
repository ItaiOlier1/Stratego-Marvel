import pygame


class Enemy:

    def __init__(self, color, pos):
        """
        constructor
        :param color:
        """
        self.color = color  # the color of the rect
        self.pos = pos
        self.img = None

    def getColor(self):
        return self.color

    def setColor(self, col):
        self.color = col

    def getRect(self):
        """
        create the enemy rect
        :return: a rect
        """
        return pygame.Rect(self.pos, (60, 45))

    def setPos(self, pos):
        self.pos = pos

    def getIMG(self):
        return self.img

    def setIMG(self, img):
        self.img = img

