num = int(input())
strings = input().split()
for i in range(len(strings)):
    if len(strings[i]) == 3: 
        if strings[i].startswith("UR"):
            strings[i] = "URI"  
        elif strings[i].startswith("OB"):
            strings[i] = "OBI"  

print(" ".join(strings))