# five percent wrong and IDK WHY

while True:
    try:
        string = input().split()
        clean_string = ''
        for i in string:
            if i.endswith('..') or not i.isalpha() or i[:len(i) -1] == '.':
                clean_string += ''
            else:
                clean_string += i + ' '

        clean_list = clean_string.split()
        words_size = 0
        for j in clean_list:
            if j.endswith('.'):
                words_size += len(j) -1
            else:
                words_size += len(j)

        if words_size > 0:  
            media = words_size // len(clean_list)
        else:
            media = 0  
            
        if media <= 3:
            points = 250
        elif  media <= 5:
            points = 500
        else:
            points = 1000
        print(points)
    except EOFError:
        break