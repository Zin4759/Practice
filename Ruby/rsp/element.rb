class Element
  attr_accessor :name
  def initialize()
    @name = []
    @status = false
  end

  def add_element(name)
    @name = name
  end

  def result
    if @status == false
      print(@name)
      print("you win!")
    end
  end
end

input = ARGV[0]
e = Element.new
e.add_element("rock")
e.add_element("scissor")
e.add_element("paper")
e.result
puts
print(input)