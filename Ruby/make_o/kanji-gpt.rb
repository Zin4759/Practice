class Kanji
  attr_accessor :letter, :meaning, :on_reading, :kun_reading

  def initialize(letter, meaning, on_reading=nil, kun_reading=nil)
    @letter = letter
    @meaning = meaning
    @on_reading = on_reading
    @kun_reading = kun_reading
  end

  def to_s
    result = "Kanji: #{@letter}, Meaning: #{@meaning}"
    result += ", On Reading: #{@on_reading}" if @on_reading
    result += ", Kun Reading: #{@kun_reading}" if @kun_reading
    result
  end
end

mountain = Kanji.new("山", "mountain", "san", "yama")
puts mountain.to_s
