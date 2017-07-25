# Ref:
# https://ruby-doc.org/core-2.2.0/doc/syntax/modules_and_classes_rdoc.html
#
# =======
# Modules
# =======
#
# Modules serves two purpose in Ruby: namespacing and mix-in functionality.
#
# == Module Definition ==
# module MyModule
#   #...
# end
#
# A module may be reopened any number of times to add, change or remove functionality:
#
# module MyModule
#   def my_method
#   end
# end
#
# module MyModule
#   alias my_alias my_method
# end
#
# module MyModule
#   remove_method :my_method
# end
#
#
# == Nesting ==
# module Outer
#   module Inner
#   end
# end
#
# module Parent::Child::GrandChild
# end
#
#
# == Scope ==
#
# == self ==
# **self** refers to the object that defines the current scope.
# **self** will change when entering a diff method or when def a new module.
#
#
# == Constants ==
# Z = 0
# module A
#   Z = 1
#   module B
#     p A::Z #=> 1
#     p ::Z  #=> 0
#   end
#   p Z  #=> 1
#   p ::Z #=> 0
# end
# puts Z #=> 0
#
#
# == Methods ==
# class method/module method/instance method/...
#
# module A
# end
#
# include A
#
# p self.class.ancestors #=> [Object, A, Kernel, BasicObject]
#
#
# == Visibility ==
# public, protected, private
#
#
# == **alias** and **undef** ==



# =======
# Classes
# =======
# Every class is also a module, but unlike modules a class may not be
# mixed-in to another module(or class).
#
# == Define Class ==
# class MyClass
#   #...
# end
#
# class MySubClasss < MyClass
# end
#
# == Inheritance ==
# class A
#   Z = 1
#   def z
#     Z
#   end
# end
# class B < A
# end
#
# p B.new.z #=> 1
#
# == Overiding ==
#
# == **super** ==
# invoke superclass functionality
#
# class A
#   def m
#     1
#   end
# end
#
# class B < A
#   def m
#     2 + super # super can take args like super(1, 2, 3)
#   end
# end
#
# p B.new.m #=> 3
#
#
# == Singleton Classes ==
# aka metaclass or eigenclass
# access the singleton class of an object using class << object
# class C
#   class << self
#     # ...
#   end
# end
# This allows definition of methods and attributes on a class (or module)
# without needing to write def self.my_method.



