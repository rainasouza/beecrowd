n = int(input())
for i in range(n):
    num = int(input())
    eh_primo = True
    for j in range(2, num -1):
        if num % j == 0:
            eh_primo = False
    if eh_primo:
        print(num,'eh primo')

    else:
        print(num,'nao eh primo')



