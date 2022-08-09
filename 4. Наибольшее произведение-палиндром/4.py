"""
Число-палиндром с обеих сторон (справа налево и слева направо)
читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""
from heapq import nlargest


palindrom=[]
un=100
while un!=999:
    for yan in range(100,1000,1):
        find = un * yan

        
        """Для 5-тизначного числа. Проверка на палиндром"""
        if len(str(find))==5:
            find=str(find)
            if ((find[0],find[1])==(find[-1],find[-2])) == True:
                palindrom.append(find)
                
                
            
        """Для 6-nизначного числа. Проверка на палиндром"""
        if len(str(find))%2==0:
            find=str(find)
            if ((find[0],find[1],find[2])==(find[-1],find[-2],find[-3])) == True:
                palindrom.append(find)
        if yan==999:
            un+=1
print(max((palindrom), key=int))
