class BoardRectangle:

    def __init__(self, rect, color, card, rect_num):
        """
        constructor:
        :param rect: the rect
        :param color: the color of the rect
        :param card: the card of the rect
        :param rect_num: the rect number (from 1 to 100)
        """
        self.rect = rect
        self.color = color
        self.card = card
        self.rect_num = rect_num

    def getRect(self):
        """
        get the card_rect
        """
        return self.rect

    def setRect(self, rect):
        """
        set the card_rect
        """
        self.rect = rect

    def getColor(self):
        """
        get the color
        """
        return self.color

    def getCard(self):
        """
        get the card
        """
        return self.card

    def setCard(self, card):
        """
        set if there is a card on(has_card)
        :param card: the card of the rect
        """
        self.card = card

    def getRect_num(self):
        """
        get the number of the rect
        """
        return self.rect_num

    def setRect_num(self, num):
        """
        set the number of the rect
        :param num: the rect number
        :return: None
        """
        self.rect_num = num
