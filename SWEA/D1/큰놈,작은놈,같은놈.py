num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    if a > b:
        print("#%d >" %(i+1))
    elif a < b:
        print("#%d <" %(i+1))
    else:        
        print("#%d =" %(i+1))