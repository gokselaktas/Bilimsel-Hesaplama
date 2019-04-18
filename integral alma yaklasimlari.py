def f(x):
    return x**2


x1 , x2 = 4, 6
n = 1000000  # araligi kac parcaya bolecegiz
h = (x2-x1)/n  # her bir dikdortgenin taban uzunlugu

#kisakenar integral
integral = 0
for i in range(n):   # alt dikdortgen toplam
   integral += f(x1 + i*h)*h
print(integral)

#uzunkenar integral
integral = 0
for i in range (1,n+1):   # ust dikdortgen toplam
    integral += f(x1+i*h)*h
print(integral)

#Bu iki metodun ortalamasi kisa-uzun
integral = 0
for i in range (n):
    integral += f(x1 + h/2 + i*h)*h
print(integral)

#Yamugun alani yardimi ile integral
integral = 0
for i in range (n):
    integral += (f(x1+i*h) + f(x1+(i+1)*h))*h/2
print(integral)
