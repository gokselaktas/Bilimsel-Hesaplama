"""
kosinüs ve sinüs fonksiyonlari sonsuz seriler ile hesaplanabilir.
cosine and sine functions can be evaluated by infinite series.

cosx = 1 - x^2/2! + x^4/4!...
sinx = x - x^3/3! + x^5/5!...
"""

from math import factorial

radian = int(input("degree: "))
PI = 3.14159265
x=radian*(PI/180) #converting radians to degrees
def cosx():
    cosx=0
    for i in range(0,100,2):
        if i%4==0:
            cosx += x**i/factorial(i)
        else:
            cosx -= x**i/factorial(i)
    return cosx

def sinx():
    sinx=0
    for i in range(1,100,2):
        if i%4==1:
            sinx += x**i/factorial(i)
        else:
            sinx -= x**i/factorial(i)
    return sinx


print("Cosinus= ",cosx())
print("Sinus= ",sinx())
