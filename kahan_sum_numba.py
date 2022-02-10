#!/usr/bin/env python3
# Kahan Summation Algorithm: https://www.geeksforgeeks.org/kahan-summation-algorithm/

import time
from numba import jit

@jit(nopython=True)
def kahanSum_forward(n):
    s = 0.0
    c = 0.0
    for f in range (1,n+1):
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
    return s

@jit(nopython=True)
def kahanSum_backward(n):
    s = 0.0
    c = 0.0
    for f in range (n,0,-1):
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
    return s

def print_result(d, key):
    print("{}:\tResult:\t{}, Time:\t{} seconds\n".format(key,*d[key]))

@jit(nopython=True)
def forward_sum(n): # Function is compiled and runs in machine code
    s = 0.0
    for i in range (1,n+1):
        s += 1/i
    return s
    #return sum(1/x for x in range(1,n+1))

@jit(nopython=True)
def reverse_sum(n): # Function is compiled and runs in machine code
    s = 0.0
    for i in range (n, 0, -1):
        s += 1/i
    return s
    #return sum(1/x for x in range(n,0,-1))

# Sum[1/i,{n,1,input}]
num = input("Number of elements (you can use scientific notation). Interesting values are 1 milion and above: ")
#converting the value into an integer
num = float(num)
num = int(num)
print("Sum[1/i,{{i,1,{}}}]\n".format(num))

results = {}

key = "Forward sum"
s = time.time()
f = forward_sum(num)
results[key]=(f,time.time()-s)
print_result(results, key)

key = "Reverse sum"
s = time.time()
r = reverse_sum(num)
results[key]=(r,time.time()-s)
print_result(results, key)

key = "Kahan Sum"
s = time.time()
k = kahanSum_forward(num)
results[key]=(k,time.time()-s)
print_result(results, key)

key = "Reverse Kahan Sum"
s = time.time()
kr = kahanSum_backward(num)
results[key]=(kr,time.time()-s)
print_result(results, key)

print("Kahan sum:\t{}\n".format(k))
print("Kahan sum differences:\t{}\n".format(k - kr))
print("Forward sum - Kahan sum:\t{}\n".format(f - k))
print("Reverse sum - Kahan sum:\t{}\n".format(r - k))
