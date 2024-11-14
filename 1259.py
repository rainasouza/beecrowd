N = int(input())
    
evens = []
odds = []
    

for i in range(N):
    num = int(input())
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
    

evens.sort()
odds.sort(reverse=True)
    

for num in evens:
    print(num)
for num in odds:
    print(num)
