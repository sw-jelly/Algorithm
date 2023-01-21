# 백준 15650번 : N과 M (2)
import sys
input = sys.stdin.readline

def dfs(graph, v, m, r):
  if len(r) == m:
    for i in r:
      print(i, end=" ")
    print()
    return

  for i in range(v, len(graph)):
    if not graph[i] in r:
      r.append(graph[i])
      dfs(graph, i, m, r)
      r.pop()

n, m = map(int, input().split())
num = []
for i in range(1, n+1):
  num.append(i)

r = []
dfs(num, 0, m, r)