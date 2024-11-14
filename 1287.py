while True:
    try:
        n = input().replace(",", "").replace(" ", "").replace("o","0").replace("O", "0").replace("l", "1")
        if not n or not n.isdigit():
            print("error")
        else:
            num = int(n)
            if num > 2147483647:
                print("error")
            else:
                print(num)

    except EOFError:
        break