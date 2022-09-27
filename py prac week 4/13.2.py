
n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

MIN = min(map(min, a))
MAX = max(map(max, a))
print('Min:', MIN, ', max:', MAX)

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
