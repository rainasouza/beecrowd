n = int(input())
for i in range(n):
    number = float(input())
    count = 0
    while number > 1:
        number /= 2
        count += 1
    print(f"{count} dias")