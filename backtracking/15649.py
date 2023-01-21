# 백준 15649번 : N과 M(1)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []
for i in range(1, n+1):
  num.append(i)

def dfs(graph, v, r):
  if len(r) == m:
    for i in range(m):
      print(r[i], end = " ")
    print()
    return

  for i in range(len(graph)):
    if not graph[i] in r:
      r.append(graph[i])
      dfs(graph, i, r)
      r.pop()
  
r = []
dfs(num, 0, r)