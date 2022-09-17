num = int(input())

for i in range(num):
    lst = list(map(int, input().split()))
    
    sum = 0
    for j in range(10):
        if lst[j] % 2 == 1:
            sum += lst[j]
    
    print("#%d %d" %(i+1, sum))