import math

while True:
    try:
        numbers = list(map(int, input().split()))
        first_factorial = math.factorial(numbers[0])
        second_factorial = math.factorial(numbers[1])
        result = first_factorial + second_factorial
        print(result)

    except EOFError:
        break