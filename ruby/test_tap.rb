# Ref:
# http://seejohncode.com/2012/01/02/ruby-tap-that/
#
# **tap method**
#
# it allows you do do something with an object inside of a block,
# and always have that block return the object itself.
#
# class Object
#   def tap
#     yield self
#     self
#   end
# end
#
# #tap was created for tapping into method chains
#
# def something
#   result = operation
#   do_something_with result
#   result # return
# end
# ==
# def something
#   operation.tap do |op|
#     do_something_with op
#   end
# end
#
# == **tap** use cases ==
# 1) Assigning a property to an object
# # TRADITIONAL
# object = SomeClass.new
# object.key = 'value'
# object
#
# # TAPPED
# object = SomeClass.new.tap do |obj|
#   obj.key = 'value'
# end
#
# # CONDENSED
# obj = SomeClass.new.tap { |obj| obj.key = 'value' }
#
# 2) Ignoring method return
# # TRADITIONAL
# object = Model.new
# object.save!
# object
#
# # TAPPED
# object = Model.new.tap do |model|
#   model.save!
# end
#
# # CONDENSED
# object = Model.new.tap(&:save!)
#
# 3) Using in-place operations chained
# # TRADITIONAL
# arr = [1, 2, 3]
# arr.reverse!
# arr
#
# # TAPPED CONDENSED
# [1, 2, 3].tap(&:reverse!)

