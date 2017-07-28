class Box
  def initialize(w, h)
      @width = w
      @height = h
      @hash = {:first=>"Michael", :last=>"Jordan"}
  end

  def get_hash
    puts @hash[:first]
  end

end

b = Box.new(3, 4)
b.get_hash
#=> Michael
