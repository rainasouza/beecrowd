n = int(input())
for i in range(n):
    text = input().strip()  
    words = text.split() 
    hidden_message = ''.join([word[0] for word in words])  
    print(hidden_message)

