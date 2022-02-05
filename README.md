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

Tested on [Intel i7-10850H CPU](https://ark.intel.com/content/www/us/en/ark/products/201897/intel-core-i710850h-processor-12m-cache-up-to-5-10-ghz.html)
