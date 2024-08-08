require 'json'

class Bubble
  attr_accessor :data

  def readjson
    file = File.read('array.json')
    data = JSON.load(file)
    @data = data["2nd"]
  end

  def swap(f_index, s_index)
    temp = @data[f_index]
    @data[f_index] = @data[s_index]
    @data[s_index] = temp
  end

  def sort
    n = @data.length
    i = 0
    while i < n
      j = 0
      while j < n-i-1
        if @data[j]>@data[j+1]
          swap(j, j+1)
        end
        j += 1
      end
      i += 1
    end
  end

  def print_result
    print(@data)
  end
end

b = Bubble.new
b.readjson
b.sort
b.print_result