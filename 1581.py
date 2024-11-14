N = int(input())
for i in range(N):
    K = int(input())
    langs = []

    for j in range(K):
        lang = input()
        langs.append(lang)

    if len(set(langs)) == 1:
        print(langs[0])

    else:
        print("ingles")