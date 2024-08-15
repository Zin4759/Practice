class Node
  attr_accessor :data, :next
  
  def initialize(data)
    @data = data
    @next = nil
  end
end

class LinkedList
  attr_accessor :head
  
  def initialize
    @head = nil
  end
  
  def append(data)
    new_node = Node.new(data)
    
    if @head.nil?
      @head = new_node
    else
      current = @head
      current = current.next until current.next.nil?
      current.next = new_node
    end
  end
  
  def to_s
    current = @head
    print "["
    while current
      print current.data
      print ", " unless current.next.nil?
      current = current.next
    end
    print "]"
  end
end
