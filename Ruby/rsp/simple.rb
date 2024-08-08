class RockScissorPaper
  attr_accessor :hand, :user_hand
  HANDS = ["rock", "scissor", "paper"]
  def generate_hand
=begin
    num = rand(1..3)
    if num == 1
      @hand = "rock"
    elsif num == 2
      @hand = "scissor"
    elsif num == 3
      @hand = "paper"
    end
    print(@hand)
=end
      # That can be Array.sample
      @hand = HANDS.sample
      puts "Computer chose: #{@hand}!"
  end

  def user_hand_receive
    if ARGV[0] == "r"
      @user_hand = "rock"
    elsif ARGV[0] == "s"
      @user_hand = "scissor"
    elsif ARGV[0] = "p"
      @user_hand == "paper"
    end
  end

  def judge
    if @hand == @user_hand
      puts("Draw!")
    elsif
      (@hand == "rock" && @user_hand == "scissor") ||
      (@hand == "scissor" && @user_hand == "paper") ||
      (@user == "paper" && @user_hand == "rock")
      puts "Computer win!"
    else
      puts("User win!")
    end
  end
end

rsp = RockScissorPaper.new
rsp.generate_hand
rsp.user_hand_receive
rsp.judge