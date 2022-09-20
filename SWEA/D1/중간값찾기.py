num = int(input())

lst = list(map(int, input().split()))
lst.sort()

mid_index = int(len(lst) / 2)

print(lst[mid_index])