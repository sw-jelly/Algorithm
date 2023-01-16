# 백준 2206번 : 벽 부수고 이동하기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited):
  visited[0][0][0] = 1
  q = deque([[0, 0, 0]])
  di = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  while q:
    x, y, wall = q.popleft()
    
    if x == n-1 and y == m-1:
      print(visited[x][y][wall])
      return

    for d in di:
      nx, ny = x+d[0], y+d[1]
      
      if 0 <= nx < n and 0 <= ny < m:
        # 갈 수 있는 땅에 방문한 적 없는 경우
        if graph[nx][ny] == 0 and not visited[nx][ny][wall]:
          visited[nx][ny][wall] = visited[x][y][wall] + 1
          q.append([nx, ny, wall])
          
        # 벽이고 벽을 한 번도 부순 적 없다면
        elif graph[nx][ny] == 1 and not wall:
          for i in di:
            if 0 <= nx+i[0] < n and 0 <= ny+i[1] < m:
              # 벽 건너가 땅이고 방문한 적 없는 경우
              if graph[nx+i[0]][ny+i[1]] == 0 and not visited[nx+i[0]][ny+i[1]][0]:
                visited[nx+i[0]][ny+i[1]][1] = visited[x][y][wall] + 2
                q.append([nx+i[0], ny+i[1], 1])
              
  print(-1)

n, m = map(int, input().split())
maze = []
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
for _ in range(n):
  maze.append(list(map(int, input().rstrip())))

bfs(maze, visited)