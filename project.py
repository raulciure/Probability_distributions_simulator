import random
import math
import numpy as np


def bernoulli(p):
    u = random.random()
    if u < p:
        return True
    else:
        return False


def binom(n, p):
    sum = 0
    u = []
    for i in range(n):
        u.append(random.random())
        if u[i] < p:
            sum += 1
    return sum


def geom_1(p):
    u = random.random()
    x = int((math.log(1-u, math.e)) / (math.log(1-p, math.e))) + 1
    return x


def geom_2(p):
    u = random.random()
    x = 1
    while u >= p:
        u = random.random()
        x += 1
    return x


def poiss(lamb):
    return np.random.poisson(lamb)


def unif_disc(n):
    u = random.random()
    return int(n * u)


def unif_cont(a, b):
    u = random.random()
    x = a+(b-a)*u
    return x


def norm(med, var):
    return np.random.normal(med, var)


def exp(theta):
    u = random.random()
    x = -theta * math.log(1-u, math.e)
    return x


while True:
    print("\nAlegeti distributia:")
    print("\n1) Bernoulli")
    print("2) Binomiala")
    print("3) Geometrica")
    print("4) Poisson")
    print("5) Uniforma discreta")
    print("6) Uniforma continua")
    print("7) Normala")
    print("8) Exponentiala")
    print("9) Iesire")

    opt = int(input("\nIntroduceti optiunea: "))
    while not opt in range(1, 10):
        opt = int(input("\nIntroduceti o optiune valida [1 -> 9]: "))

    if opt == 1:
        print("Distributia Bernoulli cuantifica succesul unui singur eveniment cu o probabilitate p.")
        p = float(input("p= "))
        while not (p <=1  and p >= 0):
            p = float(input("\nIntroduceti o probabilitate valida [0, 1]\np= "))
        print("Rezultatul simularii: x =", bernoulli(p))

    if opt == 2:
        print("Distributia binomiala cuantifica numarul de succese din n incercari asociate unui proces Bernoulli.")
        n = int(input("n (nr de incercari) = "))
        while not n >= 0:
            n = int(input("\nIntroduceti un nr. de incercari valid (>=0)\nn= "))
        p = float(input("p= "))
        while not (p <= 1 and p >= 0):
            p = float(input("\nIntroduceti o probabilitate valida [0, 1]\np= "))
        print("Rezultatul simularii: x =", binom(n, p))

    elif opt == 3:
        print("Distributia geometrica cuantifica numarul de incercari pana la primul succes, inclusiv.")
        p = float(input("p= "))
        while not (p <= 1 and p >= 0):
            p = float(input("\nIntroduceti o probabilitate valida [0, 1]\np= "))
        print("Rezultatul simularii - Metoda 1: x =", geom_1(p))
        print("Rezultatul simularii - Metoda 2: x =", geom_2(p))

    elif opt == 4:
        print("Distributia Poisson cuantifica numarul de evenimente rare ce au loc intr-o perioada de timp fixata.", "λ -> frecventa evenimentului rar")
        lamb = float(input("λ(lambda)= "))
        while not lamb > 0:
            lamb = float(input("Introduceti o valoare valida (>0)\nλ(lambda)= "))
        print("Rezultatul simularii: ", poiss(lamb))

    elif opt == 5:
        print("Distributia uniforma discreta returneaza o valoare aleatoare pe multimea {0, ..., n}.")
        n = int(input("n (elementul final al multimii)= "))
        while not n >= 0:
            n = int(input("\nIntroduceti un n valid (>=0)\nn (elementul final al multimii)4= "))
        print("Rezultatul simularii: ", unif_disc(n))

    elif opt == 6:
        print("Distributia uniforma continua cuantifica rezultatul unui experiment aleator intr-un interval [a, b].")
        a = int(input("a= "))
        b = int(input("b= "))
        if a > b:
            print("Capetele intervalului inversate!\nCorectare automata efectuata!")
            aux = a
            a = b
            b = aux
        print("Rezultatul simularii: x =", unif_cont(a, b))

    elif opt == 7:
        med = float(input("Media= "))
        var = float(input("Deviatia standard= "))
        print("Rezultatul simularii: x =", norm(med, var))

    elif opt == 8:
        print("Distributia exponentiala descrie timpii dintre evenimentele proceselor Poisson.")
        theta = float(input("θ(theta)= "))
        print("Rezultatul simularii: ", exp(theta))

    elif opt == 9:
        exit(0)
