def recurs(x, count):
    if count > 990:                 #Ограничение для рекурсии 
        return count
    
    if x == 1:
        count +=1
        return count
    
    elif x%2==0:
        x = x/2
        count +=1
        return recurs(x, count)

    else:
        x = 3 * x + 1
        count +=1
        return recurs(x, count)

count = 0

dic = {}


for _ in range(999999, 99999, -1):
    func = recurs(_, count)
    dic[_]=func
    if len(dic)>5000:
        max_val = max(dic.values())
        dic.clear() 
        dic[_]=max_val
        print(dic)
    count = 0



        


    