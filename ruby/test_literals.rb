# Ref:
# https://ruby-doc.org/core-2.2.0/doc/syntax/literals_rdoc.html
#
# Literals
#
# Literals create objects you can use in your program.
# Literals include:
#   - Booleans and nil
#   - Numbers
#   - Strings
#   - Symbols
#   - Arrays
#   - Hashes
#   - Ranges
#   - Regular Expressions
#   - Procs
#
# == Booleans and nil ==
# nil and false => false
# everything else => true
#
# == Numbers ==
#
# == Strings ==
# double-quoted string allow interpolation, escaped char and #{...} are interpolated.
# "One plus one is two: #{1 + 1}" #=> 2
#
# single-quoted raw string
# '#{1 + 1}' #=> #{1 + 1}
#
# Adjacent string literals are automatically concatenated by the interpreter:
# "con" "cat" "en" "at" "ion" #=> "concatenation"
#
# # interpolated
# multiline_str = <<HERE
# This would contain specially formatted text.
# #{1 + 1}
#
# That might span many lines
# HERE
#
# # uninterpolated
# multiline_str = <<'HERE'
# {1 + 1}
# HERE
#=> #{1 + 1}
#
#
# == Symbols ==
# A Symbol represents a name inside the ruby interpreter.
# refer to a symbol using :my_symbol
# :"my_symbol1"
# :"my_symbol#{1+1}"
#
# Note symbols are never garbage collected
#
#
# == Arrays ==
# [1, 1 + 1, 1 + 2]
# [1, [1 + 1, [1 + 2]]]
#
#
# == Hashes ==
# { "a" => 1, "b" => 2 }
# { a: 1, b: 2 }
#
#
# == Ranges ==
# (1..2)  includes ending value
# (1...2) excludes ending value
#
#
# == Regex ==
# /my regular expression/
# /my regular expression/i
#
#
# == Procs ==
# same as closure or lambda, which represents a nameless function
# -> { 1 + 1 }
# f = ->(v) { 1 + v }
# puts f.call(1) #=> 2
#
#
# == Percent Strings ==
# %(...) creates a String
# %i - Arrays of Symbols
# %q - String
# %r - Regex
# %s - Symbol
# %w - Array of Strings
# %x - Backtick
#
# escape space in percent string
# %w[one one-hundred\ one]
# #=> ["one", "one-hundred one"]
#
