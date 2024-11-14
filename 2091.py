try:
    n = int(input())  
    while n != 0:
        nums = list(map(int, input().split()))  
        alone = 0
        for num in nums:
            alone ^= num  
        print(alone)
        n = int(input())  
except EOFError:
    pass  
