values = input().split()
triangle = (float(values[0]) * float(values[2])) / 2
circle = (float(values[2]) ** 2) * 3.14159
trapezio = ((float(values[0]) + float(values[1])) * float(values[2])) / 2
sqr = float(values[1]) ** 2
rectangle = float(values[0]) * float(values[1])
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {sqr:.3f}")
print(f"RETANGULO: {rectangle:.3f}")