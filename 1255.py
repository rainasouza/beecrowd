from collections import defaultdict

N = int(input())  

for _ in range(N):
    linha = input().strip()  
    contagem = defaultdict(int)  

    
    for char in linha:
        if char.isalpha():  # Verifica se é uma letra
            contagem[char.lower()] += 1  # Conta a letra em minúscula

    # Encontra a maior frequência
    max_frequencia = max(contagem.values())
    
    # Encontra todas as letras que têm a maior frequência
    letras_frequentes = [letra for letra, count in contagem.items() if count == max_frequencia]
    
    # Ordena as letras em ordem alfabética
    letras_frequentes.sort()

    # Imprime as letras que mais ocorreram
    print("".join(letras_frequentes))