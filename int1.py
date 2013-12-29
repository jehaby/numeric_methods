from math import sqrt, sin

def f1(x):
    return 1 / sqrt(2 + 0.5 * x**2) 


a = 0.4
b = 1.2
n = 10

def f2(x):
    return sin(2*x) / x**2



def drange(start, stop, step):
    r = start
    while r <= stop:
     	yield r
     	r += step


def trap (func, a, b, n):
    """ Computes an integral of a func from a to b using """
    
    xs = [x for x in drange(a, b, (b-a) / n)]
    ys = [f1(x) for x in xs]
    
    res = sum([(ys[i] + ys[i+1]) * (xs[i+1] - xs[i]) / 2 for i in range(n)])

    return res, len(xs), n


def simpson (f, start, stop, n):

    res = 0
    i = (stop - start) / n
    a = start
    b = start + i

    while b <= stop:
        res += (b-a) * (f(a) + 4 * f((a + b) / 2) + f(b)) / 6
        a += i
        b += i

    return res




if __name__ == '__main__':
    print("Формула трапеций: ")
    print(trap(f1, a, b, n))

    print("=" * 20 + "\n")
    print("Формула Симсона: ")

    print(simpson(f2, 0.8, 1.2, 80))



