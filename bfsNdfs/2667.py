# 백준 2667번 : 단지 번호 붙이기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, x, y, visited):
  num = 0
  visited[x][y] = True
  q = deque([[x, y]])
  d = [[-1, 0], [0, -1], [1, 0], [0, 1]]

  while q:
    xy = q.popleft()
    x, y = xy[0], xy[1]
    num += 1
    for k in d:
      if 0 <= x+k[0] < n and 0 <= y+k[1] < n:
        if graph[x+k[0]][y+k[1]] == 1 and not visited[x+k[0]][y+k[1]]:
          q.append([x+k[0],y+k[1]])
          visited[x+k[0]][y+k[1]] = True
        
  return num
  
n = int(input())
a = []
visited = [[False for i in range(n)] for i in range(n)]
apart = []
r = 0

for _ in range(n):
  a.append(list(map(int, input().rstrip())))

for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and not visited[i][j]:
        apart.append(bfs(a, i, j, visited))
        r += 1
    elif a[i][j] == 0:
      visited[i][j] = 0

print(r)
apart.sort()
for asd in apart:
  print(asd)