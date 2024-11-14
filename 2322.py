n = int(input())
ns = map(int, input().split())
soma_dada = sum(ns)
soma_certa = n * (n +1) // 2
faltando = soma_certa - soma_dada
print(faltando)