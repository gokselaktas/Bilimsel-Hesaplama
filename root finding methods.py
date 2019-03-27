def f(x):
    return(x**2 - 4*x + 3)

x1 = int(input("baslangic tahmini : "))
x2 = int(input("bitis tahmini : "))

# ikiye bolerek koke yaklasiyor
def bisection_method(x1, x2):
    if (f(x1) * f(x2) == 0):
        print("tahminlerinizden biri denklemin kokudur")
    elif (f(x1) * f(x2) > 0):
        print("girdiginiz aralikta tek sayida kok yoktur ")
    else:
        xronceki = x1
        for i in range(1000):
            xr = (x1 + x2) / 2
            if (abs(f(xr) - f(xronceki)) < 0.0001):
                print("bisection buldu: ", xr, i)
                break
            elif (f(xr) * f(x1) < 0):
                x2 = xr
            else:
                x1 = xr
            xronceki = xr



#dogrusal yaklasim
def false_position_method(x1, x2):
    if (f(x1) * f(x2) == 0):
        print("tahminlerinizden biri denklemin kokudur")
    elif (f(x1) * f(x2) > 0):
        print("girdiginiz aralikta tek sayida kok yoktur ")
    else:
        xronceki = x1
        sayac = 0
        while True:
            xr = ((f(x1)*x2)-(f(x2)*x1))/(f(x1)-f(x2))
            if(abs(f(xr) - f(xronceki)) < 0.0001):
                print("false_position_method buldu: ", xr, sayac)
                break
            x1 = xr
            xronceki = xr
            sayac+=1

#tahminlerinin arasinda kok olmamasi lazim
#x1= 5 , x2=42 icin
def secant_method(x1,x2):
    if(f(x1)*f(x2) == 0):
        print("girdiginiz degerlerden biri kok")
    else:
        sayac=0
        while(abs(f(x2)-f(x1))>0.00001):
            x3 = x1 - f(x1)*(x2-x1)/(f(x2)-f(x1))
            x1,x2 = x2 ,x3
            if(x1==x2):
                break
            sayac += 1
        print(x1,sayac)


bisection_method(x1,x2)
false_position_method(x1,x2)
secant_method(x1,x2)
