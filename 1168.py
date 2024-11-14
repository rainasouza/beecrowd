n = int(input())
for i in range(n):
    number = input()
    led = 0
    for i in number:
        if i == '1':
            led += 2
        elif i in ['2', '3', '5']:
            led += 5
        elif i == '4':
            led += 4
        elif i in ['6', '9', '0']:
            led += 6
        elif i == '7':
            led += 3
        else:
            led += 7
    print(f"{led} leds")
                