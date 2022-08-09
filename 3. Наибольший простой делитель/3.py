"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143,
являющийся простым числом?
"""


from threading import Thread

b = [1, 71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633, 716151937]
a = 600851475143
a2 = 851475143
a_srez_vniz = a//2
a_srez_vverh =a_srez_vniz

def loopa(a_srez_vverh):
    for deli in range(1, a_srez_vverh, 1):
        print(a, " / ", deli, " =???", "\n")
        if a%deli==0:
            print("Возможный делитель(снизу-вверх) :", deli)
            b.append(deli)
def loopo(a_srez_vniz):
    for deli2 in range(a_srez_vniz, -1, -1):
        print(a, " / ", deli2, " =???", "\n")
        if a%deli2==0:
            print("Возможный делитель(сверху-вниз) :", deli2)
            b.append(deli2)
def pol_loopo():
    for deli3 in range(a2//2, -1, -1):
        print(a2//2, " / ", deli3, " =???", "\n")
        if a%deli3==0:
            print("Возможный делитель((сверху//2)-вниз) :", deli3)
            b.append(deli3)
def pol_loopa():
    for deli4 in range(a2//2, a2 , 1):
        print(a//2, " / ", deli4, " =???", "\t")
        if a%deli4==0:
            print("Возможный делитель((снизу(//2-внизу) :", deli4)
            b.append(deli4)
"""
Thread(target=pol_loopo()).start()
Thread(target=pol_loopa()).start()
"""
import math

def maxPrimeFactor(n):
    while n%2==0:
        max_Prime = 2
        n = n/1
    for i in range(3, int(math.sqrt(n))+1,2):
        print(i)
        while n%i==0:
            max_Prime = i
            print(max_Prime)
            n = n/i
            print(n)
                
    if n>2:
        max_Prime=n
    return int(max_Prime)
n=600851475143
print(maxPrimeFactor(n))









