N = int(input())
for _ in range(N):
    entrada = list(map(int, input().split()))
    num_notas = entrada[0]
    notas = entrada[1:]
    media_final = sum(notas)  / num_notas
    acima_da_media = 0
    for i in notas:
        if i > media_final:
            acima_da_media += 1
    percentual = (acima_da_media / num_notas) * 100
    print(f"{percentual:.3f}%")