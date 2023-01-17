# 백준 13460 : 구슬 탈출 2
# [해설 참고함] 같은 위치에 있을 때는 더 멀리 이동한 게 뒤에! 

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, rx, ry, bx, by):
  visited[rx][ry][bx][by] = True
  q = deque([[rx, ry, bx, by, 1]])
  di = [[0, 1],[1, 0],[0, -1],[-1, 0]]

  while q:
    x, y, xb, yb, k = q.popleft()
   
    if k > 10:
      break            
        
    for d in di:
      nx, ny, nbx, nby = x, y, xb, yb
      holeR = False
      holeB = False

      while True:
        nbx += d[0]
        nby += d[1]
        if graph[nbx][nby] == '#':
          nbx -= d[0]
          nby -= d[1]
          break
        elif graph[nbx][nby] == 'O':
          holeB = True
          break

      while True:
        nx += d[0]
        ny += d[1]
        if graph[nx][ny] == '#':
          nx -= d[0]
          ny -= d[1]
          break
        elif graph[nx][ny] == 'O':
          holeR = True
          break

      if holeB:
        continue
        
      if nx == nbx and ny == nby:
        if d[0] == 0:
          if abs(ny-y) > abs(nby-yb):
            ny -= d[1]
          else:
            nby -= d[1]
        else:
          if abs(nx-x) > abs(nbx-xb):
            nx -= d[0]
          else:
            nbx -= d[0]
        
      if holeR:
        if not holeB:
          print(k)
          return
      elif not visited[nx][ny][nbx][nby]:
        visited[nx][ny][nbx][nby] = True
        q.append([nx, ny, nbx, nby, k+1])
            
  print(-1)

n, m = map(int, input().split())
maze = []
# 빨강 공 기준의 visited
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
  l = list(map(str, input().rstrip()))
  maze.append(l)
  for j in range(m):
    if l[j] == 'R':
      rx, ry = i, j
    elif l[j] == 'B':
      bx, by = i, j

bfs(maze, visited, rx, ry, bx, by)