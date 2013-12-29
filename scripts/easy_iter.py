#!/usr/bin/python3
from funcs import *    


def easy_iter_f (f, k, a, b):
    print("Easy iteration's method.")

    while abs(f(b)) > E:
        b = b - f(b)/k
        print(b)
        
    return b


if __name__ == '__main__':
    x = easy_iter_f(f3, 3, 0.5, 1)
    print_results(x, f3)
