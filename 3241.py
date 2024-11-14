n = int(input())
for i in range(n):
    testes = input()
    if testes == "P=NP":
        print("skipped")
    else:
        a, b = testes.split('+')  
        a, b = int(a), int(b)  
        print(a + b)  
