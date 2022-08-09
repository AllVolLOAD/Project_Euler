"""
Выписав первые шесть простых чисел,
получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?


easy_number=[2,5]
number=1
stop=False
cheked=-1

while not stop:

    for eretosven in easy_number:
        if number%eretosven==0:
            number+=1
            break
    for any_factor in range(2,number-1):
        if number%any_factor==True:
            break
        if number%number==0:
            easy_number.append(number)
            break

    if (len(easy_number))>=10001:
        stop=True
            
    number+=1

print(easy_number)


Советом деректоров было приныто решение от 14.03.2022 :
использовать паттерны и прочие шаблоны в разработке некоммерческого ПO
"""

n = 110000
lst=[2]
for i in range(3, (n+1), 2):
    if (i > 10) and (i%10==5):
        continue
    for j in lst:
        if j*j-1 > i:
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print(lst[10000])
