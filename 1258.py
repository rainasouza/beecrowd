while True:
    num_shirts = int(input())

    if num_shirts == 0:
        break
    
    shirts = []

    for i in range(num_shirts):

        name = input()
        color_size = input().strip().split()
        color = color_size[0]
        size = color_size[1]

        shirts.append((color,size,name))

    shirts.sort(key=lambda shirt: (shirt[0], -ord(shirt[1]), shirt[2]))
    for shirt in shirts:
        print(f"{shirt[0]} {shirt[1]} {shirt[2]}")
        
    print()
