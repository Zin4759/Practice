class Info
  attr_accessor :author, :summary, :refference
  def initialize(author, summary, refference)
    @author = author
    @summary = summary
    @refference = refference
  end
end

class Card
  def initialize(:author, :summary, :refference, :opinion)
    @author = author
    @summary = summary
    @refference = refference
    @opinion = opinion
  end

end

book1 = Card.new("eco", "how to write a long book", "eco - writting paper", "This book is must read.\nBecause that book is useful.")