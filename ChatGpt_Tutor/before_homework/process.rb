class CustomProcess
  process = ["created", "Terminated", "waiting", "running", "blocked", "swapped out and wating", "swapped out and blocked"]
  attr_accessor :process_id, :arrival_time, :burst_time, :priority
  def initialize(process_id, arrival_time, burst_time, priority)
    @process_id = process_id
    @arrival_time = arrival_time
    @burst_time = burst_time
    @priority = priority
  end
end

# input
p1 = CustomProcess.new("p1", 0, 15, 3)
p2 = CustomProcess.new("p2", 5, 8, 4)
p3 = CustomProcess.new("p3", 8, 2, 1)
p4 = CustomProcess.new("p4", 10, 5, 2)