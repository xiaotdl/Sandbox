# were there same function name from parent class/mixin,
# last function will overwrite the previous one.

module A
   def a1
       puts 'a1'
   end
   def a2
       puts 'a2'
   end
end
module B
   def a1
       puts 'b1'
   end
   def b2
       puts 'b2'
   end
end

class Sample
include B
include A
   def s1
   end
end

samp=Sample.new
samp.a1
samp.a2
samp.b2
samp.s1
