import math
def simplify_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


n = int(input())


for i in range(n):
    values = input().strip().split()
    n1 = int(values[0])
    d1 = int(values [2])
    n2 = int(values[4])
    d2 = int(values[6])
    
    operation = values[3]

    match operation:
        case "+":
            num = n1*d2 + n2*d1
            den = d1 * d2
        case "-":
            num = n1*d2 - n2*d1
            den = d1*d2
        case "*":
            num = n1*n2
            den = d1*d2
        case "/":
            num = n1*d2
            den = d1*n2
    result_num = num
    result_den = den


    simp_num, simp_den = simplify_fraction(num, den)
    print(f"{result_num}/{result_den} = {simp_num}/{simp_den}")

