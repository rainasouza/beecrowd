values = input().split()
a = int(values[0])
b = int(values[1])
c = int(values[2])

if b < a and c>= b:
    print(':)')

elif b > a and c<= b:
    print(':(')

elif a < b and c > b and (c - b) < (b - a):
    print(':(')  
elif a < b and c > b and (c - b) >= (b - a):
    print(':)')  
elif a > b and c < b and (b - c) < (a - b):
    print(':)') 
elif a > b and c < b and (b - c) >= (a - b):
    print(':(')

elif a==b and c>b:
    print(':)')
elif a == b and c < b:
    print(':(')