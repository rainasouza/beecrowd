entrada = input()
if entrada.count("(") == entrada.count(")"):
    print("Partiu RU!")
else:
    while "()" in entrada:
        entrada = entrada.replace("()", "")
    assuntos = entrada.count("(")
    print(f"Ainda temos {assuntos} assunto(s) pendente(s)!")\
    
#wrong