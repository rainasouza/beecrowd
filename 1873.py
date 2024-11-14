n = int(input())
for caso in range(1,n+1):

    rajesh_wins = False
    chose = input().split()
    if chose[0] == chose[1]:
        print('empate')
        
    
    else:
        if chose[0] == 'tesoura' and chose[1] =='papel':
            rajesh_wins = True
        if chose[0] == 'papel' and chose[1] =='pedra':
            rajesh_wins = True
        if chose[0] == 'pedra' and chose[1] =='lagarto':
            rajesh_wins = True
        if chose[0] == 'lagarto' and chose[1] =='spock':
            rajesh_wins = True
        if chose[0] == 'spock' and chose[1] =='tesoura':
            rajesh_wins = True
        if chose[0] == 'tesoura' and chose[1] =='lagarto':
            rajesh_wins = True
        if chose[0] == 'lagarto' and chose[1] =='papel':
            rajesh_wins = True
        if chose[0] == 'papel' and chose[1] =='spock':
            rajesh_wins = True
        if chose[0] == 'spock' and chose[1] =='pedra':
            rajesh_wins = True
        if chose[0] == 'pedra' and chose[1] =='tesoura':
            rajesh_wins = True
        
        if rajesh_wins:
            print(f'rajesh')
            
        else:
            print(f'sheldon')