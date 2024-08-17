class Info
  attr_accessor :author, :summary, :reference
  
  def initialize(author, summary, reference)
    @author = author
    @summary = summary
    @reference = reference
  end
end

class Card
  attr_accessor :info, :opinion, :next
  
  def initialize(info, opinion)
    @info = info
    @opinion = opinion
    @next = nil
  end
end

# 사용 예시
info1 = Info.new("Umberto Eco", "How to Write a Thesis", "Eco, Umberto. How to Write a Thesis. MIT Press, 2015.")
card1 = Card.new(info1, "This book is a must-read for anyone writing a thesis. It provides practical advice and valuable insights.")

info2 = Info.new("Stephen King", "On Writing", "King, Stephen. On Writing: A Memoir of the Craft. Scribner, 2000.")
card2 = Card.new(info2, "An engaging and informative book on the craft of writing, filled with personal anecdotes and practical tips.")

card1.next = card2

# 카드 정보 출력
current = card1
while current
  puts "Author: #{current.info.author}"
  puts "Summary: #{current.info.summary}"
  puts "Reference: #{current.info.reference}"
  puts "Opinion: #{current.opinion}"
  puts "---"
  current = current.next
end
