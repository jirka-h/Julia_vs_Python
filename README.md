# Julia_vs_Python

Simple sum test comparing Python and [Julia](https://julialang.org/) Performance

```
Sum[1/i,{n,1,1e8}]
Python 3.9.9: 4.48 seconds
Julia version 1.6.4: 0.11 seconds

Python:
sum(1/x for x in range(1,num+1))

Julia:
sum(1/x for x=1:num)

./kahan_sum.py
./kahan_sum.jl
```
