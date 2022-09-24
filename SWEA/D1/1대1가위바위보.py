A, B = map(int, input().split())

# 가위 (1)
# 바위 (2)
# 보 (3)

if A == 1:
    if B == 2:
        print("B")
    elif B == 3:
        print("A")

elif A == 2:
    if B == 1:
        print("A")
    elif B == 3:
        print("B")

elif A == 3:
    if B == 1:
        print("B")
    elif B == 2:
        print("A")