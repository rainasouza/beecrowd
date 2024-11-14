is_first_case = True
while True:
    try:
        year = int(input())
        if not is_first_case:
            print()
        is_first_case = False

        is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        is_huluculu = year % 15 == 0
        is_bulukulu = is_leap and year % 55 == 0

        if is_leap:
            print("This is leap year.")
        if is_huluculu:
            print("This is huluculu festival year.")
        if is_bulukulu:
            print("This is bulukulu festival year.")
        if not (is_leap or is_huluculu or is_bulukulu):
            print("This is an ordinary year.")

    except EOFError:
        break