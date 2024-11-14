n = int(input())
total = rabbits = frogs = mouses = 0
for i in range(n):
    animals = input().split()
    qtd = int(animals[0])  
    total += qtd
    if animals[1] == 'C':
        rabbits += qtd  
    elif animals[1] == 'R':
        mouses += qtd  
    else:
        frogs += qtd  
rabbits_100 = (rabbits / total) * 100
mouses_100 = (mouses / total) * 100
frogs_100 = (frogs / total) * 100
print("Total:",total, "cobaias")
print("Total de coelhos:",rabbits)
print("Total de ratos:",mouses)
print("Total de sapos:",frogs)
print(f"Percentual de coelhos: {rabbits_100:.2f} %")
print(f"Percentual de ratos: {mouses_100:.2f} %")
print(f"Percentual de sapos: {frogs_100:.2f} %")

