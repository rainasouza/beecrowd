caso = 1  # Inicializamos a variável caso fora do loop

while True:
    try:
        num = input()
        lista = []
        
        for i in range(int(num) + 1):
            lista.extend([str(i)] * i)  # Adiciona `i` vezes o número `i` à lista
        if len(lista) + 1 == 1:
            print(f"Caso {caso}: {len(lista) + 1} numero")
        else:
            print(f"Caso {caso}: {len(lista) + 1} numeros")
        print("0 " + " ".join(lista))
        
        caso += 1  # Incrementa o número do caso
        print()
    except EOFError:
        break

#estudar mais