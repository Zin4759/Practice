require_relative 'character.rb'


class BattleJudge
  attr_accessor :participent
  def initialize()
    @participent = {}
  end

  def join_to_battle(participent)
    @participent[String(participent.name)] = [participent.hit_point, participent.attack_point]
  end

  def _attack_each_other
    sum = 0
    @participent.each do |character|
      sum = sum + character.heat_point
    end
  end
  
  def participent_two_object
    res = 0
    @participent.each do |name, stats|
      res = stats[1] - stats[2]
    end
    res
  end

  def attack_each_other
    if @participent.size >= 2
      participent_two_object
    end
    # self hit point - attack point each other
  end

  def to_s
    @participent.map do |name, stats|
      "#{name}: HP #{stats[0]}, AP #{stats[1]}"
    end.join("\n")
  end
  
end

  

aai = Character.new("Aai", 50, 45)
serina = Character.new("Serina", 55, 48)
# winia = Character.new(21, 51)

bj = BattleJudge.new()
bj.join_to_battle(serina)
bj.join_to_battle(aai)
puts bj.to_s
puts bj.participent_two_object