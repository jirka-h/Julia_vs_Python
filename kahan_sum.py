#!/usr/bin/env python3
# Kahan Summation Algorithm: https://www.geeksforgeeks.org/kahan-summation-algorithm/

import time

def kahanSum(fa):
    s = 0.0
    c = 0.0
    for f in fa:
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


# Sum[1/i,{n,1,input}]
num = input("Number of elements (you can use scientific notation). Interesting values are 1 milion and above: ")
#converting the value into an integer
num = float(num)
num = int(num)
print("Sum[1/i,{{i,1,{}}}]\n".format(num))

results = {}

key = "Forward sum"
s = time.time()
f = sum(1/x for x in range(1,num+1))
results[key]=(f,time.time()-s)
print_result(results, key)

key = "Reverse sum"
s = time.time()
r = sum(1/x for x in range(num,0,-1))
results[key]=(r,time.time()-s)
print_result(results, key)

key = "Kahan Sum"
s = time.time()
k = kahanSum(range(1,num+1))
results[key]=(k,time.time()-s)
print_result(results, key)

key = "Reverse Kahan Sum"
s = time.time()
kr = kahanSum(range(num,0,-1))
results[key]=(kr,time.time()-s)
print_result(results, key)

print("Kahan sum:\t{}\n".format(k))
print("Kahan sum differences:\t{}\n".format(k - kr))
print("Forward sum - Kahan sum:\t{}\n".format(f - k))
print("Reverse sum - Kahan sum:\t{}\n".format(r - k))
