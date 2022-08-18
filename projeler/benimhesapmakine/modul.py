def toplama(a, b):
    return a + b


def cikarma(a, b):
    return a - b


def carpma(a, b):
    return a * b


def bolme(a, b):
    return int(a) / int(b)


def karealma(a):
    return a ** 2


def karekok(a):
    return a ** 0.5


def ebob(A, B):
    bolenler = list()
    x = 1
    sonuc = 1

    while True:
        x += 1
        if A % x == 0 and B % x == 0 and x != 1:
            bolenler.append(x)
            A = A / x
            B = B / x
            x = 1
        elif A % x == 0 and x != 1:
            A = A / x
            x = 1
        elif B % x == 0 and x != 1:
            B = B / x
            x = 1
        if A == 1 and B == 1:
            for i in bolenler:
                sonuc *= i
            return sonuc
            break


def ekok(A, B):
    bolenler = list()
    x = 1
    sonuc = 1

    while True:
        x+=1
        if A%x == 0 and  B%x == 0 and x!=1:
            bolenler.append(x)
            A = A/x
            B = B/x
            x = 1
        elif A%x == 0 and x!=1:
            bolenler.append(x)

            A = A/x
            x = 1

        elif B%x == 0 and x!=1:
            bolenler.append(x)
            B = B/x
            x = 1

        if A==1 and B==1 :
            for i in bolenler:
                sonuc *= i
            return sonuc
            break


















def faktoriyel(a):
    toplam = 1
    for i in range(1, a + 1):
        toplam *= i
        i += 1

    print(toplam)
