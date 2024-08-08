require_relative 'element.rb'
require 'json'

class Rsp
  def initialize
file = File.read('data.json')
data = JSON.load(file)
reader = RspReader.new
reader.add(data["data"])
print(data)