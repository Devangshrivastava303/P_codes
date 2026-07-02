def dev_conq(n):
    for _ in range(n):
        x, y = map(int, input().split())

        if x % y == 0:
            print("YES")
        else:
            print("NO")
n=int(input())
dev_conq(n)