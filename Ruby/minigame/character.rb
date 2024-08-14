class Character
  attr_accessor :name, :hit_point, :attack_point
  def initialize(name, hit_point, attack_point)
    @name = name
    @hit_point = hit_point
    @attack_point = attack_point
  end
end