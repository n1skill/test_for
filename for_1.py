m = float(input())
p = float(input())
n = int(input())
k = (p + 100) / 100
for i in range(n):
    print(i + 1, m * k ** (i + 1 - 1))
