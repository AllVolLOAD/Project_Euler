"""
2520 - самое маленькое число,
которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""
number=2
a=100000
while number>1:
    if number==a:
        print("Опа! 100.000 пролетело! ")
        a=a*2
    if number%1==0:
         if number%2==0:
             if number%3==0:
                 if number%4==0:
                     if number%5==0:
                         if number%6==0:
                             if number%7==0:
                                 if number%8==0:
                                     if number%9==0:
                                         if number%10==0:
                                             if number%11==0:
                                                 if number%12==0:
                                                     if number%13==0:
                                                         if number%14==0:
                                                             if number%15==0:
                                                                 if number%16==0:
                                                                     if number%17==0:
                                                                         if number%18==0:
                                                                             if number%19==0:
                                                                                 if number%20==0:
                                                                                     print("Число делящееся на все:                   ", number)
                                                                                     break
    number+=1
