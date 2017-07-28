# Ruby is a pure OO language.
# Everything in Ruby is an object, including the most
# primitive type, like str, num, true/false.
# A class itself is an object to the **Class** class.
#
# A ruby class has data and methods. They are members of the class.
#
# == Define Class ==
# class CamelCase
#   code
# end
#
# == Define Object ==
# box1 = Box.new
# box2 = Box.new
#
# == initialize method ==
# # acts like constructor
# class Box
#   def initialize(w, h)
#       @width = w
#       @height = h
#   end
# end
#
# == instance variable ==
# # accessed within the class through @ operator
# # accessed outside the class through public accessor methods
#
# == accessor & setter & instance methods ==
# class Box
#   def initialize(w, h)
#       @width = w
#       @height = h
#
#   # == accessor methods ==
#   def getWidth
#       @width
#   end
#   def getHeight
#       @height
#   end
#
#   # == setter methods ==
#   def setWitdh=(value)
#       @width=value
#   end
#   def setHeight=(value)
#       @height=value
#   end
#
#   # == instance method ==
#   def getArea
#       @width * @height
#   end
#
# b = Box.new(1, 2)
# w = b.getWidth()
# h = b.getHeight()
# a = b.getArea()
# puts "The box has #{x} width, #{y} height, #{a} area."
#
#
# == class methods & variables ==
# **class variable** is shared between all instances of a class, prefixed by @@
# **class method** is defined using def self.methodname(), and called using classname.methodname.
# class Box
#   == class variable ==
#   @@count = 0
#   def initialize(w, h)
#       @width, @height = w, h
#       @@count += 1
#   end
#
#   == class method ==
#   def self.printCount()
#       puts "Box count is #@@count"
#   end
# end
#
# == to_s method ==
# class Box
#   ..
#   def to_s
#       "w:#@width, h:#@height"
#   end
# end
#
# == Access Control ==
# instance method level:
# # **public**, **private**, **protected**
#
# all methods except initialize are by default public.
# private method can't be used or view from outside the class.
# proteced method can only be used within its own or subclasses.
#
# usage e.g.
# private :getWidth, :getHeight
# protected :printArea
#
#
# == Class Inheritance ==
# Ruby does NOT support multiple inheritance, but Ruby support **mixins**
# inheritance e.g.
# derived class < base class
# subclass < superclass
#
# class Box
#   def initialize(w, h)
#       @width, @height = w, h
#   end
#   def getArea
#       @width * @height
#   end
# end
#
# class BigBox < Box
#    method overiding
#   def getArea
#       puts "calculating area"
#       super
#   end
#    add a new instance method
#   def printArea
#       puts "Big box area is #{self.getArea}."
#   end
# end
#
# bb = BigBox.new(3, 4)
# bb.getArea()
# bb.printArea()
#
#
# == Operator Overloading ==
# ...
#
#
# == Freezing Objects ==
# e.g.
# box.freeze
# if (box.frozen?)
#
#
# == Class Constant ==
# class Box
#   BOX_COMPANY = "TATA Inc"
# end
# puts Box::BOX_COMPANY
#
#
# == Class Information ==
# class Box
#   puts "Class of **self** = #{self.class}"
#   puts "Name of **self** = #{self.name}"
# end
