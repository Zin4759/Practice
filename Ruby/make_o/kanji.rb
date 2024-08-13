class Kanji
  attr_accessor :letter, :meaning, :on_reading, :kun_reading
  def initialize(letter, meaning, on_reading=None, kun_reading=None)
    @letter = letter
    @meaning = meaning
    @on_reading = on_reading
    @kun_reading = kun_reading
  end
end

mountain = Kanji.new("山", "mountain", "san", "yama")
print mountain.to_s