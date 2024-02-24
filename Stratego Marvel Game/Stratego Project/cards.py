
class Card:

    def __init__(self, name, img, pos, level, card_rect_color, board_rect):
        """
        constructor:
        :param name:  the name of the card
        :param img: the image of the card
        :param pos: the position of the card
        :param level: the level of the card
        :param card_rect_color: the color of the rect of the card
        :param board_rect: the board rectangle
        """
        self.name = name
        self.img = img
        self.pos = pos
        self.level = level
        self.card_rect = img.get_rect()
        self.card_rect_color = card_rect_color
        self.board_rect = board_rect

    def getName(self):
        """
        get the name of the card
        """
        return self.name

    def getImg(self):
        """
        get the img of the card
        """
        return self.img

    def getPos(self):
        """
        get the position of the card (x, y)
        """
        return self.pos

    def setPos(self, pos):
        """
        set the position
        :param pos:
        :return: None
        """
        self.pos = pos
        self.card_rect = self.img.get_rect()

    def getLevel(self):
        """
        get the level of the card (from 1 to 10)
        """
        return self.level

    def getCard_rect(self):
        """
        get the card_rect of the img
        """
        return self.card_rect

    def getCard_rect_color(self):
        """
        get the card;s color
        """
        return self.card_rect_color

    def setCard_rect_color(self, color):
        """
        set the card's rect color
        :param color: the color of the card
        :return:
        """
        self.card_rect_color = color

    def getRect(self):
        """
        get the board rect object of the card
        """
        return self.board_rect

    def setRect(self, rect):
        """
        set the board rect object of the card
        :param rect:
        :return: None
        """
        self.board_rect = rect



