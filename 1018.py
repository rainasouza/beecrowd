n = int(input())
print(n)

one_hundred = fifty = twenty = ten = five = two = one = 0

one_hundred = n // 100
n = n % 100

fifty = n // 50
n = n % 50

twenty = n // 20
n = n % 20

ten = n // 10
n = n % 10

five = n // 5
n = n % 5

two = n // 2
n = n % 2

one = n 

print(f"{one_hundred} nota(s) de R$ 100,00")
print(f"{fifty} nota(s) de R$ 50,00")
print(f"{twenty} nota(s) de R$ 20,00")
print(f"{ten} nota(s) de R$ 10,00")
print(f"{five} nota(s) de R$ 5,00")
print(f"{two} nota(s) de R$ 2,00")
print(f"{one} nota(s) de R$ 1,00")
