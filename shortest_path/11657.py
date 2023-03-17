# 백준 11657번 : 타임머신
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
dist = [INF] * (n+1)
edges = []
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

def bf(start):
  dist[start] = 0
  for i in range(n):
    for j in range(m):
      a, b, c = edges[j]
      if dist[a] != INF and dist[b] > dist[a] + c:
        dist[b] = dist[a] + c
        if i == n-1:
          return True
  return False

if bf(1):
  print(-1)
else:
  for i in range(2, n+1):
    if dist[i] == INF:
      print(-1)
    else:
      print(dist[i])