"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре
миллиона.
"""
summa=[]

total=0
n=0
posled=[1,2]
gotov=[]
move = True
while move:
    sled=posled[n]+posled[n+1]
    posled.append(sled)
    print("Следующее число Фибоначч :  ", sled)
    if sled%2==0:
        gotov.append(sled)
        n+=1
        if sled>4000000:
            gotov.pop(-1)
            move=False
    else:
        n+=1
gotov.append(2)
print("Список всех четных чисел :  ", gotov)
for su_m in gotov:
    total+=su_m
print("Cумма все четных чисел до 4млн. :  ", total)
    

    
    

    
    
