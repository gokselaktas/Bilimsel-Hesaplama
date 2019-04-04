from math import sqrt

#%0.0000000000000001 hassasiyet ile pi hesabi
#sonuc ~ 3.141592653589793
"""
S = altigenin bir kenarinin uzunlugu
new_S = bir sonraki cokgenin bir kenarinin uzunlugu
a = eskenar ucgenin yuksekligi
a+b = cemberin yaricapi

6'gen 12'gen 24'gen seklinde cemberin cevresine yaklasiyoruz
cevre=2.pi.r den pi =cevre/2.r (r=1)
"""
kenar = 6.0
S = 1.0
r=1.0
pi = 0.0
for i in range(500):
    S2 = S/2
    a = sqrt(1 - S2**2)
    b = 1 - a
    new_S = sqrt(b**2 + S2**2)
    P = kenar * S
    pi = P/2 * r
    #print(S2,a,b,new_S,P,pi)
    kenar *= 2
    S = new_S

print("{0:.42f}".format(pi))
