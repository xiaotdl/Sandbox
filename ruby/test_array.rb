# Ref:
# https://ruby-doc.org/core-2.2.0/Array.html
#
# Arrays are ordered, integer-indexed collections of any object.
# index 0 refers to the first item, int(length-1) or -1 refers to the last item.
#
# == Creating Arrays ==
# 1) using literal constructor []
# arr = [1, "two", 3.0]
#
# 2) explicitly calling ::new with zero, one(array.init_size),
# or two(array.init_size, default object) arguments.
# arr = Arrays.new       #=> []
# Arrays.new(3)          #=> [nil, nil, nil]
# Arrays.new(3, true)    #=> [true, true, true]
#
# 3) create array with separate objects using a block
# Arrays.new(4) {Hash.new}  #=> [{}, {}, {}, {}]
# Arrays.new(3) {Arrays.new(3)}  #=> [[nil, nil, nil], [nil, nil, nil], [nil, nil, nil]]
#
# 4) thru Kernel.Array, which tries to call to_ary, then to_a on its argument
# Array({:a => "a", :b => "b"})  #=> [[:a, "a"], [:b, "b"]]
#
#
# == Accessing Elements ==
# 1) elements in an array can be retrived using the #[] method
# arr = [1, 2, 3, 4, 5, 6]
# arr[2] #=> 3
# arr[100] #=> nil
# arr[-2] #=> 5
# arr[2, 4] #=> [3, 4, 5, 6] # second arg is offset
# arr[1..4] #=> [2, 3, 4, 5]
# arr[0..-1] #=> [1, 2, 3, 4, 5, 6]
#
# 2) using **at** method
# arr.at(0) #=> 1
#
# 3) **fetch** method, provides default value when index is outside of array bounds
# arr.fetch(100, 'oops') #=> "oops"
#
# == special methods ==
# **first**
# a.first   #=> 1
# **last**
# a.last    #=> 6
# **take** return first n elements of an array
# a.take(3) #=> [1, 2, 3]
# **drop** return elements after droping first n elements
# a.drop(3) #=> [4, 5, 6]
#
#
# == Obtain Array Info ==
# browsers = ['Chrome', 'Firefox', 'Safari', 'Opera', 'IE']
# browsers.length   #=> 5
# browsers.count    #=> 5
# browsers.empty?   #=> false
# browsers.include?('Konqueror') #=> false
#
#
# == Adding Items to Array ==
# arr = [1, 2, 3, 4]
# arr.push(5)       #=> [1,2,3,4,5] # add to the end
# arr << 6          #=> [1,2,3,4,5,6]
# arr.unshift(0)    #=> [0,1,2,3,4,5,6] # add to the beginning
# arr.insert(3, 'apple')    #=> [0, 1, 2, 'apple', 3, 4, 5, 6]
# arr.insert(3, 'orange', 'pear', 'grapefruit') #=> ...
#
#
# == Removing Items from Array ==
# arr =  [1, 2, 3, 4, 5, 6]
# arr.pop           #=> 6 #=> [1, 2, 3, 4, 5]
# arr.shift         #=> 1 #=> [2, 3, 4, 5]
# arr.delete_at(2)  #=> 4 #=> [2, 3, 5]
#
# arr = [1, 2, 2, 2, 3]
# arr.delete(2)     #=> 2 #=> [1, 3]
#
# **arr.compact** remove nil values
# **arr.compact!** remove nil values in place
# arr = [1, nil, 3]
# arr.compact #=> [1, 3]  # arr unchanged
# arr.compact! #=> [1, 3] # arr changed in place
#
# **arr.uniq** returns uniq set
# **arr.uniq!** returns uniq set in place
# arr = [1, 2, 2, 3]
# arr.uniq #=> [1, 2, 3]  # arr unchanged
# arr.uniq! #=> [1, 2, 3] # arr changed in place
#
#
# == Interating over Array ==
# Like all classes include the **Enumerable** module (as a mixin),
# Array has an **each** method, which yields elements to the supplied block in sequence.
# == **each** method ==
# arr = [1, 2, 3, 4, 5]
# arr.each { |a| print a - 10, " " } #=> -9 -8 -7 -6 -5
#
# == **reverse_each** method ==
# words = %w[first second third fourth fifth sixth]
# str = ""
# words.reverse_each { |word| str += "#{word} " }
# p str #=> "sixth fifth fourth third second first "
#
# == **map** method ==
# arr.map { |a| 2*a }  #=> [2, 4, 6, 8, 10] # arr unchanged
# arr.map! { |a| 2*a } #=> [2, 4, 6, 8, 10] # arr changed in place
#
#
# == Selecting Items from Array ==
# arr = [1, 2, 3, 4, 5, 6]
# arr.select { |a| a > 3 }      #=> [4, 5, 6]
# arr.reject { |a| a < 3 }      #=> [3, 4, 5, 6]
# arr.drop_while { |a| a < 3 }  #=> [3, 4, 5, 6]


