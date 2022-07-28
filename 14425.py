n, m = map(int, input().split())

s = set()
for _ in range(n):
    s.add(input())

out = 0
for _ in range(m):
    if input() in s:
        out += 1

print(out)