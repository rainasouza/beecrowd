n = int(input())
for i in range(n):
    opened = 0
    diamonds = 0
    values = input().strip()
    for i in values:
        if i == "<":
            opened += 1
        elif i == ">" and opened >0:
            opened -= 1
            diamonds +=1
    print(diamonds)

