class Dice
  attr_accessor :side_of_dice

  def initialize(maximum_sides)
    @maximum_sides = maximum_sides
    @side_of_dice = (1..@maximum_sides).to_a
  end

  def roll
    @side_of_dice.sample
  end
end

dice = Dice.new(6)
puts dice.roll
