import math


def toplama(a, b):
    return a + b


def cikartma(a, b):
    return a - b


def carpma(a, b):
    return a * b


def bolme(a, b):
    return a / b


def kokalma(a):
    return math.sqrt(a)


def karealma(a):
    return math.pow(a, 2)


def sayiyuvarlama(a):
    return math.ceil(a)


def faktoriyel(a):
    return math.factorial(a)


def ebob(a, b):
    return math.gcd(a, b)


def sinus(a):
    return math.sin(math.radians(a))


def cosinus(a):
    return math.cos(math.radians(a))


def tanjant(a):
    return math.tan(math.radians(a))


print(50 * "*")
print("yapmak istediğiniz işlemi seçiniz:\n")
print("1-toplama işlemi")
print("2-çıkartma işlemi")
print("3-çarpma işlemi")
print("4-bölme işlemi")
print("5-karekök alma işlemi")
print("6-kare işlemi")
print("7-sayı yuvarlama işlemi")
print("8-faktöriyel işlemi")
print("9-ebob bulma işlemi")
print("10-bir sayının sinüsünü bulma işlemi")
print("11-bir sayının cosinusünü bulma işlemi")
print("12-bir sayının tanjantını bulma işlemi")
print(50 * "*")



while True:
    secim = input("yapmak istediğiniz işlemin numarasını giriniz:")
    



    if secim == "q" or secim == "Q":
        print("uygulamadan çıkış yaptınız")
        break

    elif secim == "1":
        a = int(input("birinci sayı :"))
        b = int(("ikinci sayı :"))
        print(toplama(a, b))
    elif secim == "2":
        a = int(input("birinci sayı :"))
        b = int(input("ikinci sayı :"))
        print(cikartma(a, b))

    elif secim == "3":
        a = int(input("birinci sayı :"))
        b = int(("ikinci sayı :"))
        print(carpma(a, b))

    elif secim == "4":
        a = int(input("birinci sayı :"))
        b = input(("ikinci sayı :"))
        print(bolme(a, b))

    elif secim == "5":
        a = int(input("kökünü bulmak istediğiniz sayıyı giriniz :"))
        print(kokalma(a))

    elif secim == "6":
        a = int(input("karesi alınacak sayıyı giriniz:"))
        print(karealma(a))

    elif secim == "7":
        a = float(input("yuvarlamak istediğiniz sayıyı giriniz:"))
        print(sayiyuvarlama(a))

    elif secim == "8":
        a = int(input("faktöriyeli bulunacak sayıyı giriniz:"))
        print(faktoriyel(a))

    elif secim == "9":
        a = int(input("ebob için birinci sayıyı giriniz:"))
        b = int(input("ebob için ikinci sayıyı girirniz:"))
        print(ebob(a, b))

    elif secim == "10":
        a = int(input("sinüsü bulunacak  sayıyı giriniz:"))
        print(sinus(a))

    elif secim == "11":
        a = int(input("cosinüsü bulunacak sayıyı giriniz:"))
        print(cosinus(a))

    elif secim == "12":
        a = int(input(" tanjantı bulunacak sayıyı sayıyı giriniz:"))
        print(tanjant(a))

    else:
        print("geçersiz bir işlem sayısı girdiniz")
