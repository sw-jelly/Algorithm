import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))


for i in range(n):
  if i == 0:
    s = [l[i]]
  else:
    s.append(s[i-1] + l[i])

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  if (a == 1):
    print(s[b-1])
  else:
    print(s[b-1] - s[a-2])
