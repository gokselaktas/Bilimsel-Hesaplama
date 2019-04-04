#
#dogrusal interpolasyon
x=[1,2,3,4,6,7,9]   # f(x)=y --- len(x)==7 --- sum(x)==32
y=[3,5.5,7.2,9,14,15,19]

xiyi = 0
for i in range(len(x)):
    xiyi += x[i]*y[i]
# xiyi yi tek satirda nasil yazabiliriz
# xiyi = sum([x[i]*y[i] for i in range(len(x))])

a1 = (len(x)*xiyi - sum(x)*sum(y))/(len(x)*sum([i**2 for i in x])-sum(x)**2)
a0 = (sum(y)-a1*sum(x))/len(x)
print(a0,a1)
