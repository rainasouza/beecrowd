notas = list(map(float, input().split()))
media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + notas[3]) / 10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    nova_media = (media + exame) / 2
    if nova_media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {nova_media:.1f}')
else:
    print('Aluno reprovado.')
