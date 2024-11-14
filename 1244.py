n = int(input())
def sizing(e):
    return len(e)

for i in range(n):
    sentece = list(input().split())
    sentece.sort(key=sizing, reverse=True)
    final_sentece = ' '.join(sentece)
    print(final_sentece)