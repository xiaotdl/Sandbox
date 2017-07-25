# Ref:
# https://ruby-doc.org/core-2.2.0/Hash.html#method-c-5B-5D
#
# Hash
# A Hash is a dictionary-like collection of unique keys and their values.
# AKA Associative Arrays.
#
# == Create Hash ==
# grades = { "Jane Doe" => 10, "Jim Doe" => 6 }
# ==
# options = { :font_size: 10, :font_family: "Arial" }
# ==
# options = { font_size: 10, font_family: "Arial" }
#
# options[:font_size]  # => 10
#
# grades = Hash.new
# grades["Dorothy Doe"] = 9
#
# == set default value ==
# grades = Hash.new(0)
# grades = {"Timmy Doe" => 8}
# grades.default = 0
#
#
# == Common Usage ==
# books         = {}
# books[:matz]  = "The Ruby Language"
# books[:black] = "The Well-Grounded Rubyist"
#
# Hashes are also commonly used as a way to have named parameters in functions.
# If a hash is the last argument on a method call, no braces are needed.
# Note that no brackets are used below.
#
# Person.create(name: "John Doe", age: 27)
#
# def self.create(params)
#   @name = params[:name]
#   @age  = params[:age]
# end
#
#
# ====================
# Public Class Methods
# ====================
# ...
#
# == has_key?(key)
# h = { "a" => 100, "b" => 200  }
# h.has_key?("a")   #=> true
# h.has_key?("z")   #=> false
#
# == include?(key) ==
# alias has_key? include?
