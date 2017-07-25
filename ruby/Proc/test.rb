def gen_times(factor)
    return Proc.new {|n| n*factor}
end

times3 = gen_times(3)

puts times3.call(12)
# >>>
# 36
