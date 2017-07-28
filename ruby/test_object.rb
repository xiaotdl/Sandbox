class Fred
  def initialize(p1, p2)
    @a, @b = p1, p2
  end
end

fred = Fred.new('cat', 99)
puts fred.instance_variable_set(:@a, 'dog')   #=> "dog"
puts fred.instance_variable_set(:@c, 'cat')   #=> "cat"
puts fred.inspect                             #=> "#<Fred:0x401b3da8 @a=\"dog\", @b=99, @c=\"cat\">"
