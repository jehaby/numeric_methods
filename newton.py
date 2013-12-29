#!/usr/bin/python3
from funcs import *    

def newton (a, b, f, df, e = 0.001):
    """ newton """
    print("newton")
    print(a, b)

    while abs(f(b)) > e:
        b = b - f(b)/df(b)
        print(b)
        
    return b


def print_results (x):
    print("\n\n","="*20,"\nf(x) = ", f(x))
    print("x=", x)

if __name__ == '__main__':
    x2 = newton(1, 2, f , df)
    print_results(x2)
