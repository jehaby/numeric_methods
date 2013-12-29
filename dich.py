#!/usr/bin/python3
from funcs import *

def is_same_sign (a, b):
    """ """
    if a == 0 or b == 0: return False
    return abs(a) / a == abs(b) /b 

rc = 0
    

def dichf (f, a, b):
    """ """
    print(a,'    ', b, end = '   x = ')
    
    x = (b - a) / 2 + a
    print(x)
    
    if abs(f(x)) < E: return x
    
    if is_same_sign(f2(a), f2(x)):
        return dichf(f, x, b)
    else:
        return dichf(f, a, x)

if __name__ == '__main__':
    print(dichf(f2, 1, 2))
    #    print(f2(1), f2(2), f2(1.5))