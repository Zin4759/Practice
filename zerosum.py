class GameTheory:
    def __init__(self, user1, user2):
        self.participant1 = user1
        self.participant2 = user2
        pass

class ZeroSum(GameTheory):
    def __init__(self, user1, user2, entire_pie):
        super().__init__(user1, user2)
        self.entire_pie = entire_pie
        pass

game = GameTheory("roller", "thyer")
zero = ZeroSum("roller", "thyer", 80)

print(game.participant1, game.participant2)
print(zero.participant1, zero.participant2, zero.entire_pie)
