from math import factorial

def calc_e():
    n=100
    e=1
    for i in range(1,n+1):
        e += (1/float(factorial(i)))
    return e


def e_pow_x():
    e = 0
    x = 5
    for i in range(100):
        e += x**i/float(factorial(i))
    return e

def e_pow_minus_x():
    e = 0
    x = 5 # x = -5
    for i in range(100):
        if i%2 == 0:
            e += x**i/float(factorial(i))
        else:
            e -= x**i/float(factorial(i))
    return e

print(calc_e())
print(e_pow_x())
print(e_pow_minus_x())
