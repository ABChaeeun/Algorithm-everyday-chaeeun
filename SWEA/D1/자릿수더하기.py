num = int(input())

a = int(num / 1000)
b = int(num / 100 % 10)
c = int(num / 10 % 10)
d = int(num % 10)

print(a + b + c + d)