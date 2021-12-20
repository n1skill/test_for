m = int(input())
n = int(input())
for i in range(m + 1, n, -1):
    if i % 2 == 0 and m > n:
        print(i - 1)
