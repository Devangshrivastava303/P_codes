n, f = map(int, input().split())

baseline = 0
gains = []
for i in range(n):
    k, l = map(int, input().split())
    normal = min(k, l)
    doubled = min(2*k, l)
    baseline += normal
    gains.append(doubled - normal)

gains.sort(reverse=True)
total = baseline + sum(gains[:f])
print(total)