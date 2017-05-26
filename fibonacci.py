#!/usr/bin/env python3

# Lab 16: recursion
# Fibonacci with cache

import sys
sys.setrecursionlimit(5000000)

global fib_cache
fib_cache = {}  # Dictionary



def fib(n):
    if n == 0:
        return 0
    elif n in fib_cache:
        return fib_cache.get(n)
    elif n == 1:
        return 1
    else:
        x = fib(n-1) + fib(n-2)
        fib_cache[n] = x
        return x



