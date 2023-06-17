class Game:
    def __init__(self, user1, user2):
        self.participant1 = user1
        self.participant2 = user2
        pass

class Theory:
    def __init__(self, author): # author = Author of the paper or theory
        self.author = author
        pass

class GameTheory(Game, Theory):
    def __init__(self, user1, user2, entire_pie, author):
        Game.__init__(self, user1, user2)
        self.entire_pie = entire_pie
        Theory.__init__(self, author)
        pass
