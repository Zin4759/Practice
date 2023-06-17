from gametheory import *


class ZeroSum(GameTheory):
    def __init__(self, user1, user2, entire_pie, author):
        super().__init__(user1, user2, entire_pie, author)
        #self.entire_pie = entire_pie
        pass

if __name__ == "__main__":
    zero = ZeroSum("roller", "thyer", 80, "I want none")
    adgame = GameTheory("roller", "begger", 90, "Neumann")
    print(zero.participant1, zero.participant2, zero.entire_pie)
    print()
    print(adgame.participant1, adgame.participant2, adgame.entire_pie, adgame.author)
