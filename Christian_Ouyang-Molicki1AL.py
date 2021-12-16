# from random import choice, seed

# while True:
#     try:
#         number = int(input("Podaj swój numer w dzienniku: "))
#         if 1 <= number <= 28:
#             break
#         else:
#             print("Podaj liczbę z zakresu 1 - 28!")
#     except ValueError:
#         print("Podaj poprawnie swój numer w dzienniku!")

# seed(number * 33 + 551)
# tasks = [i for i in range(1,22)]
# my_tasks = []
# for i in range(5):
#     n = choice(tasks)
#     tasks.remove(n)
#     my_tasks.append(n)
#
# my_tasks.sort()
#
# print("\nWykonaj zadania: ")
# for i in my_tasks:
#     print(f"Zadanie {i}")

# Wykonaj zadania:
# Zadanie 9
# Zadanie 10
# Zadanie 11
# Zadanie 16
# Zadanie 20

def zad9(s):
    a = len(s)
    n = 0
    for el in s:
        n += el
        print(a/n)


def zad10(a):
    samo = "iyeaouąęó"
    spol = "bcćdfghjklłmnprstwzżź"
    liczbsam = 0
    liczbspol = 0
    for el in a:
        if el in samo:
            liczbsam += 1
        elif el in spol:
            liczbspol += 1
    print(f"Jest {liczbsam} samogłosek i {liczbspol} spółgłosek")



def zad11(a):
    l = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
    f = "123456789"
    a = a.lower()
    a_l = len(a)
    l_l = 0
    f_l = 0
    for el in l:
        for el_a in a:
            if el == el_a:
                l_l += 1
    for el1 in f:
        for el_a1 in a:
            if el1 == el_a1:
                f_l += 1
    unk = a_l - f_l - l_l
    krt = (l_l, f_l, unk)
    print(krt)


def zad16(a, b, c):
    d  = 0
    if b == "+":
        d = a + c
    elif b == "-":
        d = a - c
    elif b == "*":
        d = a * c
    elif b == chr(92):
        d = a / c
    print(f"{a} {b} {c} jest równe: {d}")
# przykład zad16(5, "*", 10)

def zad20(a, b):
    i = 1
    c = 0
    f = b
    while c < b:
        f -=1
        t = ' '*f
        g = f"{a}"*i
        print(t+g)
        i += 2
        c += 1