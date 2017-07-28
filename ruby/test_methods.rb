# Ref:
# https://ruby-doc.org/core-2.2.0/doc/syntax/methods_rdoc.html
#
# Methods
#
# == Method Names ==
# Method names may end with:
# - a ! (bang or exclamation mark)
# - a ? (question mark)
# - a = equals sign.
#
# By convention:
# ! method => change data in place.
# ? method => return boolean.
# = method => assignment method.

# Note that for assignment methods the return value will
# always be ignored. Instead the argument will be returned:
# def a=(value)
#   return 1 + value
# end
# p(a = 5) # prints 5
#
#
# == Scope ==
#
# = add a method to an object =
# greeting = "Hello"
# def greeting.broaden
#   self + ", world!"
# end
# greeting.broaden #=> "Hello, world!"
#
# A method defined like this is called a “singleton method”.
# *broaden* will only exist on the string instance greeting.
# Other strings will not have broaden.
#
#
# **self** is a keyword referring to the current object
# under consideration by the compiler.
# puts self #=> main
#
#
# == Overriding ==
#
#
# == Arguments ==
# def add_one(value)
#   value + 1
# end
#
# The parentheses around the arguments are optional:
# def add_one value
#   value + 1
# end
#
# Multiple args:
# def add_values(a, b)
#   a + b
# end
#
#
# == Array/Hash/Block Arguments ==
#
# def my_method(&my_block)
#   my_block.call(self)
# end
# ==
# def my_method
#   yield self
# end
#
# def each_item(&block)
#   @items.each(&block)
# end
#
#
# == Exception Handling ==
# Methods have an implied exception handling block.
# def my_method
#   begin
#     # code that may raise an exception
#   rescue
#     # handle exception
#   end
# end
# ==
# def my_method
#   # code that may raise an exception
# rescue
#   # handle exception
# end
