"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,
то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""
n=0
su_m = []
su_mready=[]
for i in range(0,1001,1):
    su_m.append(i)
for io in su_m:
    if su_m[n]%3==0:
        su_mready.append(io)
        n=n+1
    elif su_m[n]%5==0:
        su_mready.append(io)
        n=n+1
    else:
        n+=1
print(sum(su_mready)-1000)    

