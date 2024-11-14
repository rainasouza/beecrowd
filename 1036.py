import math
values = input().split()
a = float(values[0])
b = float(values[1])
c = float(values[2])

if a == 0:
    print("Impossivel calcular")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        
        # Exibe as raízes
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")