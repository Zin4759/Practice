class Game:
    def __init__(self, user1, user2):
        self._user1 = user1
        self._user2 = user2
        pass

class Theory:
    def __init__(self, author): # author = Author of the paper or theory
        self._author = author
        pass

# 다중 상속을 이용하여 개념을 구현하려고 함.

class GameTheory(Game, Theory):
    def __init__(self, user1, user2, entire_pie, author):
        Game.__init__(self, user1, user2)
        self._entire_pie = entire_pie
        Theory.__init__(self, author)
        pass
