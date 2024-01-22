n, k = map(int,input().split())
coins = []

for i in range(n):
    coins.append(int(input()))
    coins.sort(reverse=True)

ans = 0
for j in coins:
    if k >= j:
        ans += k//j
        k %= j
        if k <= 0:
            break
print(ans)