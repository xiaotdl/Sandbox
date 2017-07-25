# Ref:
# https://ruby-doc.org/core-2.2.0/doc/syntax/calling_methods_rdoc.html
# == Calling Method ==
# Calling a method sends a message to an object so it can perform some work.
# my_method()
# the parenthesis are optional:
# my_method
#
# ========
# Receiver
# ========
# **self** is the default receiver.
# my_object.my_method
# This sends *my_method* message to *my_object*.
# *NoMethodError* will be raised if the object has no such method.
#
# =========
# Arguments
# =========
# There are 3 types of arguments:
#   1) positional args
#   2) keyword(or named) args
#   3) block arg
# Each message sent may use one, two, or all types of args.
# But the args must be specified in this order.
# All args in ruby are passed by reference and are not lazily evaluated.
#
# == positional args ==
# my_method(1, '2', :three)
# def my_method(a, b = 2, c = 3, d)
#   p [a, b, c, d]
# end
#
# == hash args ==
# my_method('a' => 1, b: 2, 'c' => 3)
#
# == block arg ==
# The block argument sends a closure from the calling scope to the method.
# A block is sent to a method using do ... end or { ... }:
# A block will accept arguments from the method it was sent to.
# my_method do |argument1, argument2|
#   # ...
# end
#
#
# == Array to Arguments Conversion ==
# args = [1, 2, 3]
# my_method(*args)
# is same as =>
#
# args = [2, 3]
# my_method(1, *args)
# is same as =>
#
# my_method(1, 2, 3)
# <=
#
# def my_method(a, b, c: 3)
# end
# arguments = [1, 2, { c: 4 }]
# my_method(*arguments)
#
#
# == Hash to Keyword Arguments Conversion ==
# arguments = { first: 3, second: 4, third: 5  }
# my_method(**arguments)
# is same as =>
#
# arguments = { first: 3, second: 4  }
# my_method(third: 5, **arguments)
# is same as =>
#
# my_method(first: 3, second: 4, third: 5)
# <=
#
# If the method definition uses ** to gather arbitrary keyword arguments,
# they will not be gathered by *:
# def my_method(*a, **kw)
#   p arguments: a, keywords: kw
# end
# my_method(1, 2, '3' => 4, five: 6)
# #=> {:arguments=>[1, 2, {"3"=>4}], :keywords=>{:five=>6}}
#
#
# == Proc to Block Conversion ==
# # convert a proc or lambda to a block arg using & op.
# def my_method
#   yield self
# end
# argument = proc { |a| puts "#{a.inspect} was yielded" }
# my_method(&argument)
# #=> main was yielded
#
# =============
# Method Lookup
# =============
# Here is the order of method lookup for the receiver’s class or module R:
# - The prepended modules of R in reverse order
# - For a matching method in R
# - The included modules of R in reverse order
#
#
#
#
