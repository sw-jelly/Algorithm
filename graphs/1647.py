# 백준 1647번 : 도시 분할 계획
import sys
input = sys.stdin.readline

def find(p, x):
  if p[x] != x:
    p[x] = find(p, p[x])
  return p[x]

def union(p, a, b):
  a = find(p, a)
  b = find(p, b)

  if a < b:
    p[b] = a
  else:
    p[a] = b

edges = []
r = 0
max = 0

n, m = map(int, input().split())
p = [0] * (n+1)

for i in range(1, n):
  p[i] = i

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find(p, a) != find(p, b):
    union(p, a, b)
    if cost > max:
      max = cost
    r += cost

print(r-max)