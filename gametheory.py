from resource_pie import *

class Game:
    # 게임 = 게임이론에서의 게임적인 부분을 담당할 예정
    def __init__(self, user1, user2):
        self._user1 = user1
        self._user2 = user2
        pass
    def join(self, newbie):
        # 임시로 만든 함수임.
        # 아무래도 스택의 개념이 포함될 것 같다.
        self._newbie = newbie
        pass

class Theory:
    # 이론 = 게임이론에서의 룰을 담당할 예정? 
    # 조만간 제외하거나 새로운 기능으로 변형할듯
    def __init__(self, author): # author = Author of the paper or theory
        self._author = author
        pass

# 다중 상속을 이용하여 개념을 구현하려고 함.

class GameTheory(Game, Theory):
    # 이곳에 pie(resource) 클래스의 인스턴스를 매개변수로 주려고 함.
    def __init__(self, user1, user2, pie_value, author):
        Game.__init__(self, user1, user2)
        self._entire_pie = whole_resource(pie_value)
        Theory.__init__(self, author)
        pass
    # 프로퍼티를 이용해서 self.entire_pie를 관리할 예정


if __name__ == "__main__":
    pie = whole_resource(50)
    print(pie.resource)
    pie.more_input = 30
    print(pie.resource)

    game = GameTheory("test1", "test2", 30, "von")