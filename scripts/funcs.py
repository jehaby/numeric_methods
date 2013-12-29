E = 0.001

E = 0.001

def f3 (x):
    """ solution between 0.5 to 1. 5"""
    return x**3 + 0.4*x**2 + 0.6*x - 1.6
    

def f(x):

    return x**3 + x - 5

def df(x):
    """ returns df """
    return 3*x**2 + 1

def ff(x):
    return x**3 + 3*x*x - 3

def dff(x):
    return 3*x*x + 6*x


f2 = f

    
def print_results (x, f):
    print("\n\n","="*20,)
    print("F({0}) == {1}".format(x, f(x)))
