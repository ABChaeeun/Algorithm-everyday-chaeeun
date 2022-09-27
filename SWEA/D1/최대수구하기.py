num = int(input())

for i in range(1, num+1):
    lst = list(map(int, input().split()))
    
    max = lst[0]
    for j in range(len(lst)):
        if max < lst[j]:
            max = lst[j]

    print('#%d %d' %(i, max))