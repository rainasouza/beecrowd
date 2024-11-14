N = int(input())
for _ in range(N):
    word1, word2 = input().split()
    result = ""
    minimum = min(len(word1), len(word2))
    for i in range(minimum):
        result+= word1[i] + word2[i]
    result += word1[minimum:] + word2[minimum:]
    print(result)

