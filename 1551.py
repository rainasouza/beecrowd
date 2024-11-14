n = int(input())
for i in range(n):
    unique = set()
    sentece = input()
    for i in sentece:
        if i.isalpha():
            unique.add(i)

    if len(unique) == 26:
        print("frase completa")
    elif len(unique) >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")





        


