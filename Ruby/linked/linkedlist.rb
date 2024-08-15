class LinkedList
  attr_accessor :pointer
  def initialize
    @pointer
  end

  def point_to(target)
    @pointer = target
  end

  def to_s
    puts "point to #{@pointer}"
  end
end

first_node = LinkedList.new
second_node = LinkedList.new

first_node.point_to(second_node)
first_node.to_s