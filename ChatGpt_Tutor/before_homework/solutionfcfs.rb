class FcfsCpu
  attr_accessor :cpu_queue, :waiting_time, :execution_order

  def initialize
    @current_time = 0
    @cpu_queue = []
    @waiting_time = []
    @execution_order = []
  end

  def add_to_queue(ps)
    @cpu_queue << ps
  end

  def sort_within_arrival_time
    @cpu_queue.sort_by! { |ps| ps.arrival_time }
  end

  def calculate_to_burst_time
    @cpu_queue.each do |ps|
      @execution_order << ps.process_id
      @current_time += ps.burst_time
    end
  end

  def calculate_to_waiting_time
    start_time = 0
    @cpu_queue.each do |ps|
      wait_time = start_time - ps.arrival_time
      @waiting_time << wait_time
      start_time += ps.burst_time
    end
  end

  def calculate_to_average_time
    @waiting_time.sum / @waiting_time.size.to_f
  end

  def print_start_sequence
    puts "실행 순서: #{@execution_order.join(' -> ')}"
  end

  def print_waiting_times
    @cpu_queue.each_with_index do |ps, i|
      puts "#{ps.process_id} 대기: #{@waiting_time[i]}초"
    end
  end

  def print_average_waiting_time
    puts "평균 대기시간: #{calculate_to_average_time}초"
  end
end

class CustomProcess
  attr_accessor :process_id, :arrival_time, :burst_time, :priority

  def initialize(process_id, arrival_time, burst_time, priority)
    @process_id = process_id
    @arrival_time = arrival_time
    @burst_time = burst_time
    @priority = priority
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

cpu.sort_within_arrival_time
cpu.calculate_to_burst_time
cpu.calculate_to_waiting_time
cpu.print_start_sequence
cpu.print_waiting_times
cpu.print_average_waiting_time
