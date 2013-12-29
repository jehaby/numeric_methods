from math import factorial as fac

xi = [0.1217, 0.1736, 0.1141, 0.185]  

x = .115
y = 8.65729


xs = list(map(lambda x: x / 1000,
              range(115, 181, 5)))


ys = [8.65729, 8.29329, 7.95829, 7.64893, 7.36235, 7.09613, 6.84815,\
      6.61659, 6.39986, 6.19658, 6.00551, 5.82558, 5.65583, 5.49543]


d = dict(zip(xs, ys))


def get_diff(l):
    res = []
    for i in range(len(l) - 1):
        res.append(l[i+1] - l[i])
    return res


d1y = get_diff(ys)
d2y = get_diff(d1y)
d3y = get_diff(d2y)


def get_index_x(x, xs = xs):
    nl = [abs(x - xi) for xi in xs]
    return nl.index(min(nl))
    

def int_newton_1(x):
    i = get_index_x(x)
    x0 = xs[i]
    y0 = ys[i]

    q = ((x - x0) / .005)

    res = y0 + q * d1y[i] + q * (q-1) * d2y[i] / 2 + \
          q * (q-1) * (q-2) * d3y[i]/6
    
    return res


def int_newton_2(x):
    i = get_index_x(x)
    xn = xs[i]
    yn = ys[i]

    q = ((x - xn) / .005)

    res = yn + q * d1y[i-1] + q * (q+1) * d2y[i-2] / 2 + \
          q * (q+1) * (q+2) * d3y[i-3]/6
    
    return res

    
if __name__ == '__main__':
    print("f({:.3f}) == {:.5f}".format(xi[2], int_newton_1(xi[2])))
    print("f({:.3f}) == {:.5f}".format(xi[0], int_newton_1(xi[0])))
    print("f({:.3f}) == {:.5f}".format(xi[1], int_newton_2(xi[1])))
    print("f({:.3f}) == {:.5f}".format(xi[3], int_newton_2(xi[3])))
    print(xs)
    

    
    
    
    
    
    



        
        
    


