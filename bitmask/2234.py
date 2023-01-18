# 백준 2234번 : 성곽
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, room, x1, y1):
  visited[x1][y1] = room
  q = deque([[x1, y1]])
  k = 1
  
  while q:
    x, y = q.popleft()

    if not graph[x][y] & 8:
      if not visited[x+1][y]:
        visited[x+1][y] = room
        q.append([x+1, y])
        k += 1
        
    if not graph[x][y] & 4:
      if not visited[x][y+1]:
        visited[x][y+1] = room
        q.append([x, y+1])
        k += 1
          
    if not graph[x][y] & 2:
      if not visited[x-1][y]:
        visited[x-1][y] = room
        q.append([x-1, y])
        k += 1

    if not graph[x][y] & 1:
      if not visited[x][y-1]:
        visited[x][y-1] = room
        q.append([x, y-1])
        k += 1

    if not q:
      return(k)
      

n, m = map(int, input().split())
castle = []
size = [0]
visited = [[0 for _ in range(n)] for _ in range(m)]
room, big, big2 = 0, 0, 0

for _ in range(m):
  castle.append(list(map(int, input().split())))

for i in range(m):
  for j in range(n):
    if not visited[i][j]:
      room += 1
      tmp = bfs(castle, visited, room, i, j)
      size.append(tmp)
      if tmp > big:
        big = tmp

di = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for i in range(m):
  for j in range(n):
    for d in di:
      nx, ny = i+d[0], j+d[1]
      if 0 <= nx < m and 0 <= ny < n:
        tmp = size[visited[nx][ny]] + size[visited[i][j]]
        if visited[nx][ny] != visited[i][j] and tmp > big2:
          big2 = tmp
          
print(room)
print(big)
print(big2)