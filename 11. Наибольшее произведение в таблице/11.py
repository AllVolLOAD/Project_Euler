# type is str

calcul = 0

with open("it.txt", "r") as readit:
    print("1. File is open")
    for _ in readit:
        calcul += int(_)
    print("result :", calcul)
        
        
