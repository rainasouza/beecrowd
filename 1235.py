N = int(input())

for _ in range(N):
    sentece = input()

    half1 = sentece[:len(sentece)//2]
    half2 = sentece[len(sentece)//2:]

    print(half1[::-1] + half2[::-1])