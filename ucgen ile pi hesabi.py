import math
# pi sayisi hesabi yaklasik %3 hassasiyet ile

r = 1
                               # sonaci degiskeni kosinus teoreminin uygulandigi kucuk ucgenin acisini tutuyor
def ucgen_method_icerden():    #cemberin icine r*kok3 kenarina sahip eskenar ucgen cizerek cemberin cevresini bulmaya calisiyoruz
    aci  = 120
    uzunkenar = r*(3**0.5)
    pi = 0
    for i in range(1000):      #53. adimdan sonra sonaci hep 180 derece oluyor
        sonaci = (360 - aci)/2 #acida 0'a cok yakin olmasina ragmen python 0 olarak isleme dahil ediyor
        x = (uzunkenar/(1 + math.cos(sonaci)))**0.5 #kosinus teoreminde uzun kenari ve aciyi biliyoruz
        aci /= 2
    pi += (3 * x)/2
    #print(format(pi, ".10g"))
    return pi

def ucgen_method_disardan():
    kisakenar = r/(3**0.5) # altigenin kenarinin yarisi
    aci = 120
    pi = 0
    for i in range(100):
        sonaci = (360 - aci)/2
        x = (2*(kisakenar**2)*(1+math.cos(sonaci)))**0.5#kosinus teoreminde kisa kenar ve aciyi biliyoruz
        aci /= 2
    pi += (12 * x)/2
    return pi

print("iceriden ucgen method = ", ucgen_method_icerden())
print("disaridan ucgen methid=", ucgen_method_disardan())
