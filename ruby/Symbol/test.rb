# Ref:
# https://ruby-doc.org/core-2.0.0/Symbol.html
#
# Symbol
#
# Symbol is unique to ruby interpreter.
#
# == Create Symbol ==
# :name
# :"str"
# to_sym()


# The same Symbol object will be created for a given name or string
# for the duration of a program's execution, regardless of the context
# or meaning of that name.
#
# module One
#     class Fred
#     end
#     $f1 = :Fred
# end
#
# module Two
#     Fred = 1
#     $f2 = :Fred
# end
#
#
# # current module
# def Fred()
# end
# $f3 = :Fred
#
# puts One::Fred.class
# puts Two::Fred.class
# # #=>
# # Class
# # Fixnum
#
# puts $f1
# puts $f1.object_id
# puts $f1.class
# # #=>
# # Fred
# # 405868
# # Symbol
#
# puts $f2
# puts $f2.object_id
# puts $f2.class
# # #=>
# # Fred
# # 405868
# # Symbol
#
# puts $f3
# puts $f3.object_id
# puts $f3.class
# # #=>
# # Fred
# # 405868
# # Symbol
#
# puts "all symbols: #{Symbol.all_symbols.size}"
# puts "all symbols: " + Symbol.all_symbols.size.to_s
# puts Symbol.all_symbols.class
# puts Symbol.all_symbols.empty?
# # #=>
# # all symbols: 2306
# # all symbols: 2306
# # Array
# # false
#
#
# ====================
# Public Class Methods
# ====================
#
# == all_symbols => array ==
# Symbol.all_symbols.size    #=> 903
# Symbol.all_symbols[1,20]   #=> [:floor, :ARGV, :Binding, ...]
#
# =======================
# Public Instance Methods
# =======================
#
# == symbol <=> other_symbol → -1, 0, +1 or nil, on whether lt, eq, gt ==
#
# == inspect → string ==
# returns the representation of sym as a symbol literal
#
# == to_proc ==
# (1..3).collect(&:to_s)  #=> ["1", "2", "3"]
#
#
#
#
#
