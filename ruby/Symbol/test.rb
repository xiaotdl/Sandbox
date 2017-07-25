# Ref:
# https://ruby-doc.org/core-2.0.0/Symbol.html
# symbol is unique to ruby interpreter

module One
    class Fred
    end
    $f1 = :Fred
end

module Two
    Fred = 1
    $f2 = :Fred
end


# current module
def Fred()
end
$f3 = :Fred

puts One::Fred.class
puts Two::Fred.class
puts "=="

puts $f1
puts $f1.object_id
puts $f1.class
puts "=="

puts $f2
puts $f2.object_id
puts $f2.class
puts "=="

puts $f3
puts $f3.object_id
puts $f3.class
puts "=="

puts "all symbols: #{Symbol.all_symbols.size}"
puts "all symbols: " + Symbol.all_symbols.size.to_s
puts Symbol.all_symbols.class
puts Symbol.all_symbols.empty?
# >>>
# ==
# all symbols: 2306
# all symbols: 2306
# Array
# false

# >>>
# Class
# Fixnum
# ==
# Fred
# 405868
# Symbol
# ==
# Fred
# 405868
# Symbol
# ==
# Fred
# 405868
# Symbol

