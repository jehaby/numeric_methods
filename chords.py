#!/usr/bin/python3
from funcs import *    

def chords (a, b, e = 0.001):
    """chords"""
    a1 = a - f(a)*(a-b)/(f(a)-f(b))
    
#    while abs(a-a1) > e:
    while abs(f(a)) > e:
        a = a1
        a1 = a - f(a)*(a-b)/(f(a)-f(b))
        print(a, b)
        print("a-b: ", a-b)
        
    return a

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
    
    """    
    x = chords(1, 2, E)
    
    x1 = newton(-2, -1, ff, dff)
    """
    x2 = newton(-2, -1, f , df)


   
    print_results(x2)

    