require_relative 'process'

class FcfsCpu
  @time_slice = 4
  attr_accessor :cpu_queue, :waitng_time, :execution_order
  def initialize
    @current_time = 0
    @cpu_queue = []
    @waitng_time = []
    @execution_order = []
  end

  def add_to_queue(ps)
    @cpu_queue << ps.process_id
  end

  def sort_within_arrival_time
  end

  def calculate_to_burst_time
  end

  def calculate_to_waiting_time
  end

  def calculate_to_average_time
  end


  def print_start_sequence
    print "실행 순서 "+String(@cpu_queue)
  end
end

p1 = CustomProcess.new("p1", 0, 15, 3)
p2 = CustomProcess.new("p2", 5, 8, 4)
p3 = CustomProcess.new("p3", 8, 2, 1)
p4 = CustomProcess.new("p4", 10, 5, 2)

cpu = FcfsCpu.new
cpu.add_to_queue(p1)
cpu.add_to_queue(p2)
cpu.add_to_queue(p3)
cpu.add_to_queue(p4)
cpu.print_start_sequence