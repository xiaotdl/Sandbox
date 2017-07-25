# Ref:
# https://ruby-doc.org/core-2.2.0/Enumerable.html
#
# Enumerable
#
# The Enumerable mixin provides collection classes with several
# traversal and searching methods, and with the ability to sort.
#
# The class must provide a method **each**, which yields
# successive members of the collection.
#
# Enumerable#max, #min, or #sort is used, the objects in the collection
# must also implement a meaningful <=> operator, as these methods
# rely on an ordering between members of the collection.
#
# =======================
# Public Instance Methods
# =======================
#
# == all? [{ |obj| block } ] → true or false ==
# Iterate through all elements, returns true if the block nevers returns
# false or nil.
# If the block is not given, Ruby adds an implicit block of { |obj| obj },
# which will cause all? to return true when none of elements are false or nil.
#
# %w[ant bear cat].all? { |word| word.length >= 3 } #=> true
# [nil, true, 99].all?                              #=> false
#
# == any? [{ |obj| block }] → true or false ==
# Iterate through all elements, returns true if the block ever returns
# a value other than false or nil
#
# ...
#
