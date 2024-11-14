N = int(input())
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(N):
    encrypted = input()
    shift = int(input())
    result = ""

    for i in encrypted:
        pos = abc.index(i)
        new_pos = (pos - shift) % 26
        result += abc[new_pos]
    print(result)
