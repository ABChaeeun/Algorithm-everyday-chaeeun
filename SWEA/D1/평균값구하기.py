num = int(input())

for i in range(num):

    num_list = list(map(int, input().split()))

    sum = 0
    for j in range(len(num_list)):
        sum += num_list[j]
    print("#%d %d" % (i + 1, round(sum / len(num_list))))