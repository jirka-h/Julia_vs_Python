#!/bin/bash
#=
exec julia --color=yes --startup-file=no "${BASH_SOURCE[0]}" "$@"
=#

function kahanSum(fa)
  s = 0.0
  c = 0.0
  for f in fa
    y = 1/f - c
    t = s + y

    # Algebraically, c is always 0
    # when t is replaced by its
    # value from the above expression.
    # But, when there is a loss,
    # the higher-order y is cancelled
    # out by subtracting y from c and
    # all that remains is the
    # lower-order error in c

    c = (t - s) - y
    s = t
  end
  return s
end


# Sum[1/i,{i,1,input}]
print("Number of elements (you can use scientific notation). Interesting values are 1 milion and above: ")
num = readline()
num = parse(Float64, num)
num = trunc(Int, num)
println("Sum[1/i,{{n,1,", num, "}]")

println("Forward sum")
@time f = sum(1/x for x=1:num)
println(f)

println("Reverse sum")
@time r = sum(1/x for x=num:-1:1)
println(r)

println("Kahan sum")
@time k = kahanSum(1:num)
println(k)

println("Reverse Kahan Sum")
@time kr = kahanSum(num:-1:1)
println(kr)

println("Kahan sum differences:\t", k - kr)
println("Forward sum - Kahan sum:\t", f - k)
println("Reverse sum - Kahan sum:\t", r - k)

