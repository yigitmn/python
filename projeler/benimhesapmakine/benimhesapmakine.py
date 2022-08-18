from modul import *

print(50 * "*")
print("yapmak istediğiniz işlemi seçiniz:\n")
print("1-toplama işlemi")
print("2-çıkartma işlemi")
print("3-çarpma işlemi")
print("4-bölme işlemi")
print("5-karekök alma işlemi")
print("6-kare işlemi")
print("7-faktöriyel işlemi")
print("8-ebob bulma işlemi")
print("9-ekok bulma işlemi")
print(50 * "*")

while True:
    secim = input("yapmak istediğiniz işlemin numarasını giriniz:")

    if secim == "q" or secim == "Q":
        print("uygulamadan çıkış yaptınız")
        break

    elif secim == "1":
        a = int(input("birinci sayı :"))
        b = int(input("ikinci sayı:"))
        print(toplama(a, b))
    elif secim == "2":
        a = int(input("birinci sayı :"))
        b = int(input("ikinci sayı :"))
        print(cikarma(a, b))

    elif secim == "3":
        a = int(input("birinci sayı :"))
        b = int(input("ikinci sayı :"))
        print(carpma(a, b))

    elif secim == "4":
        a = int(input("birinci sayı :"))
        b = int(input("ikinci sayı :"))
        print(bolme(a, b))

    elif secim == "5":
        a = int(input("kökünü bulmak istediğiniz sayıyı giriniz :"))
        print(karekok(a))

    elif secim == "6":
        a = int(input("karesi alınacak sayıyı giriniz:"))
        print(karealma(a))



    elif secim == "7":
        a = int(input("faktöriyeli bulunacak sayıyı giriniz:"))
        faktoriyel(a)


    elif secim == "8":
        a = int(input("ebob için birinci sayıyı giriniz:"))
        b = int(input("ebob için ikinci sayıyı girirniz:"))
        print(ebob(a, b))

    elif secim == "9":
        a = int(input("ekok için birinci sayıyı giriniz:"))
        b = int(input("ekok için ikinci sayıyı girirniz:"))
        print(ekok(a, b))




    else:
        print("geçersiz bir işlem sayısı girdiniz")
