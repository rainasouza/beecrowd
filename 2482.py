n = int(input())
dicionario = {}
for i in range(n):
    idioma = input()
    traducao = input()
    dicionario[idioma]=traducao
m = int(input())
for i in range(m):
    nome = input()
    nacionalidade = input()
    print(nome)
    print(dicionario[nacionalidade])
    print()

    