# 백준 2606번 : 바이러스

def bfs(x):
  visited[x] = True
  q.append(x)
  if len(com[x]):
    for c in com[x]:
      if not visited[c]:
        r.append(c)
        bfs(c)

import sys

n = int(input())
net = int(input())
com = [([]) for _ in range(n+1)]
visited = [True] + [False] * n
r = []
q = []

for _ in range(net):
  n, k = map(int, sys.stdin.readline().split())
  com[n].append(k)
  com[k].append(n)


bfs(1)
result = set(r)
print(len(result))