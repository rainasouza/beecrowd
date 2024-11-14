while True:
    try:
        values = input()
    except EOFError:
        break
    open_p = 0
    valid = True
    for i in values:
        if i == "(":
            open_p += 1 
        elif i == ")":
            if open_p > 0:
                open_p -= 1
            else:
                valid = False
                break
            
    if open_p == 0 and valid:
        print("correct")
    else:
        print("incorrect")
                
    