# 백준 2252번 : 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

n, m  = map(int, input().split())
graph = [[] for _ in range(n+1)]
ind = [0] * (n+1)

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  ind[b] += 1

def tsort():
  r = []
  q = deque()

  for i in range(1, n+1):
    if ind[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    r.append(now)

    for i in graph[now]:
      ind[i] -= 1
      if ind[i] == 0:
        q.append(i)

  return r

r = tsort()
for i in r:
  print(i, end=" ")
print()