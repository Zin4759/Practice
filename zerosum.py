class Game:
    def __init__(self, user1, user2):
        self.participant1 = user1
        self.participant2 = user2
        pass

class Theory:
    def __init__(self, author): # author = Author of the paper or theory
        self.author = author
        pass

class GameTheory:
    def __init__(self, user1, user2):
        self.participant1 = user1
        self.participant2 = user2
        pass

class AdvancedGameTheory(Game, Theory):
    def __init__(self, user1, user2, entire_pie, author):
        Game.__init__(self, user1, user2)
        self.entire_pie = entire_pie
        Theory.__init__(self, author)
        pass

class ZeroSum(GameTheory):
    def __init__(self, user1, user2, entire_pie):
        super().__init__(user1, user2)
        self.entire_pie = entire_pie
        pass

game = GameTheory("roller", "thyer")
zero = ZeroSum("roller", "thyer", 80)

adgame = AdvancedGameTheory("roller", "begger", 90, "Neumann")

print(game.participant1, game.participant2)
print(zero.participant1, zero.participant2, zero.entire_pie)
print()
print(adgame.participant1, adgame.participant2, adgame.entire_pie, adgame.author)
