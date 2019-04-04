from math import sqrt
import math

#%0.0000000000000001 hassasiyet ile pi hesabi

"""
S = altigenin bir kenarinin uzunlugu
new_S = bir sonraki cokgenin bir kenarinin uzunlugu
a = eskenar ucgenin yuksekligi
a+b = cemberin yaricapi

6'gen 12'gen 24'gen seklinde cemberin cevresine yaklasiyoruz
cevre=2.pi.r den pi =cevre/2.r (r=1)
"""
def icerden_yaklasim():
    kenar = 6.0
    S = 1.0
    r=1.0
    pi = 0.0
    for i in range(500):
        S2 = S/2
        a = sqrt(1 - S2**2)
        b = 1 - a
        new_S = sqrt(b**2 + S2**2)
        cevre = kenar * S
        pi = cevre/2 * r
        #print(S2,a,b,new_S,P,pi)
        kenar *= 2
        S = new_S

    print("{0:.42f}".format(pi))
    return pi

def disardan_yaklasim():
    kenar = 6.0
    S = 1.0
    r=1.0
    pi = 0.0
    for i in range(500):
        S2= S/2
        a = sqrt(1 - S2**2)
        b = 1 - a
        new_S = sqrt(b**2 + S2**2)
        cevre = 1/a*kenar * S
        pi = cevre/2

        kenar *= 2
        S = new_S
    print("{0:.42f}".format(pi))
    return pi



icerden_yaklasim()               #3.141592653589793560087173318606801331043243
disardan_yaklasim()              #3.141592653589793560087173318606801331043243
print("{0:.42f}".format(math.pi))#3.141592653589793115997963468544185161590576
