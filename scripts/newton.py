#!/usr/bin/python3
from funcs import *    

def newton (a, b, f, df):
    """ newton """
    print("Newton's method.'")

    while abs(f(b)) > E:
        b = b - f(b)/df(b)
        print(b)
        
    return b

    
if __name__ == '__main__':
    x2 = newton(1, 2, f , df)
    print_results(x2, f)
