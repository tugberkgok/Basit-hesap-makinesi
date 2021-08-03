def topla(p1,p2):
    c = p1 + p2
    return c
def böl(p1,p2):
    if p1<p2:
        a="HATALI GİRİS"
        return a
    c = p1/p2
    return c
def carp(p1,p2):
    c = p1*p2
    return c
def çıkart(p1,p2):
    c =p1-p2
    return c
cevap = input("Yapılmak istenen işlem nedir? \nToplama, \nCıkarma \nBolme \nCarpma\n")
if cevap == "Toplama":
    x = int(input("ilk sayı"))
    y = int(input("ikinci sayı"))
    sonuc = topla(x,y)
    print(sonuc)
elif cevap == "Bolme":
    x = int(input("ilk sayı"))
    y = int(input("ikinci sayı"))
    sonuc = böl(x,y)
    print(sonuc)
elif cevap == "Cıkarma":
    x = int(input("ilk sayı"))
    y = int(input("ikinci sayı"))
    sonuc = çıkart(x,y)
    print(sonuc)
elif cevap == "Carpma":
    x = int(input("ilk sayı"))
    y = int(input("ikinci sayı"))
    sonuc = carp(x, y)
    print(sonuc)
else:
    print("HATALI GİRİS")
