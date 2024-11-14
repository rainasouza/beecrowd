n = int(input())
for caso in range(1,n+1):

    sheldon_wins = False
    chose = input().split()
    if chose[0] == chose[1]:
        print(f'Caso #{caso}: De novo!')
        
    
    else:
        if chose[0] == 'tesoura' and chose[1] =='papel':
            sheldon_wins = True
        if chose[0] == 'papel' and chose[1] =='pedra':
            sheldon_wins = True
        if chose[0] == 'pedra' and chose[1] =='lagarto':
            sheldon_wins = True
        if chose[0] == 'lagarto' and chose[1] =='Spock':
            sheldon_wins = True
        if chose[0] == 'Spock' and chose[1] =='tesoura':
            sheldon_wins = True
        if chose[0] == 'tesoura' and chose[1] =='lagarto':
            sheldon_wins = True
        if chose[0] == 'lagarto' and chose[1] =='papel':
            sheldon_wins = True
        if chose[0] == 'papel' and chose[1] =='Spock':
            sheldon_wins = True
        if chose[0] == 'Spock' and chose[1] =='pedra':
            sheldon_wins = True
        if chose[0] == 'pedra' and chose[1] =='tesoura':
            sheldon_wins = True
        
        if sheldon_wins:
            print(f'Caso #{caso }: Bazinga!')
            
        else:
            print(f'Caso #{caso}: Raj trapaceou!')
        
