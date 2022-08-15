# 백준 1260번 : DFS와 BFS
from collections import deque
import sys

def dfs(graph, v, visited):
  visited[v] = True
  print(v+1, end=" ")

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  q = deque()
  q.append(v)
  visited[v] = True
  print(v+1, end=" ")
  
  while q:
    vi = q.popleft()
    
    for i in graph[vi]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        print(i+1, end=" ")

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] * n for _ in range(n)]
visited = [False] * n

for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x-1].append(y-1)
  graph[y-1].append(x-1)

# 작은 수의 노드를 먼저 방문할 수 있도록
for i in range(n):
  graph[i].sort()

dfs(graph, v-1, visited)
print()
visited = [False] * n
bfs(graph, v-1, visited)
print()