#soru-1
"""
sayi = int(input("bir sayı giriniz:"))

if(sayi > 0):
    print("girdiğiniz sayı pozitif bir sayı")
    
elif(sayi<0):
    print("girdiğiniz sayı negatif bir sayı")
    
else:
    print("girdiğiniz sayı nötr bir sayı")
"""
###############################################################################    
#soru-2
"""
mat = int(input("matematik ortalamanızı giriniz:"))    
edebiyat = int(input("edebiyat ortalamanızı giriniz:"))
biyoloji = int(input("biyoloji ortalamanızı giriniz:"))
fizik = int(input("fizik ortalamanızı giriniz:"))
kimya = int(input("kimya ortalamanızı giriniz:"))
tarih = int(input("tarih ortalamanızı giriniz:"))
cografya = int(input("coğrafya ortalamanızı giriniz:"))

ortalama = ((mat+edebiyat+biyoloji+fizik+kimya+tarih+cografya)/7)

if(ortalama>=50):
    print("geçtiniz")
    
else:
    print("kaldınız")
"""    
###############################################################################
#soru-3
"""
while(True):
    
    a = int(input("a sayısını giriniz:"))
    b = int(input("b sayısını giriniz:"))

    if(a>b):
        print("a sayısı b sayısından büyüktür")

    if(b>a):
        print("b sayısı a sayısından büyüktür")
        
    if(a==b):
        print("a ve b sayısı eşittir\n")
"""        
###############################################################################     
#soru-4
"""
while(True):
    
    a = int(input("a sayısını giriniz:"))
    b = int(input("b sayısını giriniz:"))

    if(a>b):
        print("a sayısı b sayısından büyüktür")

    elif(b>a):
        print("b sayısı a sayısından büyüktür")
        
    else(a==b):
        print("a ve b sayısı eşittir\n")
"""    
###############################################################################
#soru-5                 
"""
sayi1 = 12         #çıktı 240 olur
sayi2 = 60
toplam = 0

if(sayi1<=sayi2):
    if(sayi1%2==0):
        sayi1==sayi2
        toplam = sayi1+sayi2
        print(toplam)
    
    else:
        toplam=sayi2-sayi1
        toplam+=toplam
        print(toplam)
"""
###############################################################################
#soru-6
"""
sayi1 = 40         #çıktı  olur
sayi2 = 13
toplam = 0

if(sayi1<=sayi2):
    if(sayi1%2==0):
        sayi1==sayi2
        toplam = sayi1+sayi2
        print(toplam)
    
    else:
        toplam=sayi2-sayi1
        toplam+=toplam
        print(toplam)
"""
###############################################################################
#soru-7
"""
print("-"*30)
print("1-İlkbahar")
print("2-yaz")
print("3-sonbahar")
print("4-kış")
print("-"*30)

mevsim = int(input("1 ila 4 arasında bir sayı giriniz:"))

if(mevsim==1):
    print("bu mevsimde ortalama sıcaklık 15 derecedir")
    
elif(mevsim==2):
    print("bu mevsimde ortalama sıcaklık 26 derecedir")
    
elif(mevsim==3):
    print("bu mevsimde ortalama sıcaklık 14 derecedir")
    
else:
    print("bu mevsimde ortalama sıcaklık 5 derecedir")
 """   
############################################################################### 
#soru-8
"""
while(True):
    
    a = input("a kenarını giriniz:")
    b = input("b kenarını giriniz:")
    c = input("c kenarını giriniz:")
    d = input("d kenarını giriniz:")

    if(a==b==c==d):
        print("bu bir kare")
    
    elif(a==b and c==d):
        print("bu bir dikdörtgen")
    
    elif(a==c and b==d):
        print("bu bir diktdörtgen")
    
    elif(a==d and b==c):
        print("bu bir dikdörtgen")
    
    else:
        print("herhangi bir dörtgen\n\n")
"""   
############################################################################### 
#soru-9    
"""   
a = int(input(" a sayısını gitiniz:"))
b = int(input(" b sayısını gitiniz:"))
c = int(input(" c sayısını gitiniz:"))
    
if(a<=b+c and b<=a+c and c<=a+b):
    if(a==b==c):
      print("bu eşkenar bir üçgen")
    elif(a==b):
            print("bu ikizkenar bir üçgen")
        
    elif(a==c):
            print("bu ikizkenar bir üçgen")
            
    elif(b==c):
            print("bu ikizkenar bir üçgen")
            
    else:
            print("bu herhangi bir üçgen\n")
           
else:
    print("bu kenarlar bir üçgen belirtmiyor")
"""            
###############################################################################          
 #soru-10
"""
boy = float(input("boyunuzu giriniz:(örenk 1.70)"))
kilo = float(input("kilonuzu giriniz:(örnek 69.7)"))
ke = kilo/(boy**2)

if(ke<18):
    print("zayıf")
if(ke>18 and ke<=25):
    print("normal")
if(ke<25 and ke<=30):
    print("kilolu")
if(ke>30):
    print("100 lv. didcord moderatörü")
"""   
    
    
            
            
            
            
            
            
        


























