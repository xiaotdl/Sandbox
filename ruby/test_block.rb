# Ref:
# https://mixandgo.com/blog/mastering-ruby-blocks-in-less-than-5-minutes
#
# Block
#
# == Define Block ==
# two ways of defining a block
# 1) do ... end
# 2) { ... }
#
# [1, 2, 3].each do |n|
#   puts "Number #{n}"
# end
# ==
# [1, 2, 3].each {|n| puts "Number #{n}"}
#
# |n| - block parameter
#
# == yield() == same as block.call()
# e.g. 1
# def my_method
#   puts "reached the top"
#   yield
#   yield
#   puts "reached the bottom"
# end
#
# my_method do
#   puts "reached yield"
# end
#
# #=>
# reached the top
# reached yield
# reached yield
# reached the bottom
#
# e.g.2
# def my_method
#   r = yield("John", 2)
#   puts r
# end
#
# my_method do |name, age|
#   "#{name} is #{age} years old."
# end
#
# == block_given? ==
# used to check whether a block is given to a method?
#
# == block.call() == same as yield()
# def my_method(&block)
#   puts block #=> #<Proc:0x007ff0a01731b0@test_block.rb:55>
#   r = block.call
#   puts r
# end
#
# my_method { "Hello!" }
# #=> #<Proc:0x007ff0a01731b0@test_block.rb:55>
# #=> Hello!
#
#
# == .map(&:something) ==
# .map(&:capitalize)
# ==
# .map { |title| title.capitalize }
# the Symbol class implements **to_proc** method which turns :capitalize into {|x| x.capitalize}
#
#
# == iterator ==
# def my_map(array)
#   new_array = []
#
#   for element in array
#     new_array.push yield element
#   end
#
#   new_array
# end
#
# def my_map(array, &times2)
#   new_array = []
#
#   for element in array
#     new_array.push(yield(element))
#     # ==
#     new_array.push(times2.call(element))
#   end
#
#   new_array
# end
#
# new_array = my_map([1, 2, 3]) do |x|
#  x * 2
# end
# print new_array, " "
# => [2, 2, 4, 4, 6, 6]
#
# == init objects with default values ==
# class Car
#   attr_accessor :color, :doors
#
#   def initialize
#     yield(self)
#   end
# end
#
# car = Car.new do |c|
#   c.color = "Red"
#   c.doors = 4
# end
#
# puts "My car's color is #{car.color} and it's got #{car.doors} doors."
#
# == block use cases ==
# basically used as closure/callback that is to be invoked later
#
# e.g.1
# def wrap_in_tags(tag, text)
#   html = "<#{tag}>#{text}</#{tag}>"
#   yield html
# end
#
# wrap_in_tags("title", "Hello") { |html| Mailer.send(html) }
# wrap_in_tags("title", "Hello") { |html| Page.create(:body => html) }
#
# e.g.2
# class Note
#   attr_accessor :note
#
#   def initialize(note=nil)
#     @note = note
#     puts "@note is \"#{@note}\""
#   end
#
#   def self.create
#     self.connect
#     note = new(yield)
#     note.write
#     self.disconnect
#   end
#
#   def write
#     puts "Writing \"#{@note}\" to the database..."
#   end
#
# private
#
#   def self.connect
#     puts "Connecting to the database..."
#   end
#
#   def self.disconnect
#     puts "Disconnecting from the database..."
#   end
# end
#
# Note.create { "I got a brilliant idea." }
# #=>
# Connecting to the database...
# @note is "I got a brilliant idea."
# Writing "I got a brilliant idea." to the database.
# Disconnecting from the database...
#
# == find divisible elements of an array ==
# class Fixnum
#   def to_proc
#     Proc.new do |obj, *args|
#       obj % self == 0
#     end
#   end
# end
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].select(&3)
# print numbers, " "
# #=> 3, 6, 9
