"""
Следовательно,
разность между суммой квадратов и
квадратом суммы первых десяти натуральных чисел составляет
3025 − 385 = 2640.
Найдите разность между суммой квадратов и
квадратом суммы первых ста натуральных чисел.
"""
un_lst= []
yan_lst= []
for un in range(1,101,1):
    un_lst.append(un)
sum_box=sum(un_lst)**2
for yan in range(1,101,1):
    yan=yan**2
    yan_lst.append(yan)
box_sum=sum(yan_lst)
print(sum_box-box_sum)


