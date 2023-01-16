# 백준 2178번 : 미로 탐색

# 미로 최소 경로 : bfs
# 큐에 해당 칸까지 온 칸 수를 같이 저장

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited):
  visited[0][0] = True
  q = deque([[0, 0, 1]])
  di = [[0, 1], [1, 0], [-1, 0], [0, -1]]

  while q:
    xy = q.popleft()
    x, y, k = xy[0], xy[1], xy[2]
    
    for d in di:
      if 0 <= x+d[0] < n and 0 <= y+d[1] < m:
        if x+d[0] == n-1 and y+d[1] == m-1:
          visited[x+d[0]][y+d[1]] = True
          print(k+1)
          return
        elif graph[x+d[0]][y+d[1]] == 1 and not visited[x+d[0]][y+d[1]]:
          visited[x+d[0]][y+d[1]] = True
          q.append([x+d[0], y+d[1], k+1])
    
      

n, m = map(int, input().split())
maze = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
  maze.append(list(map(int, input().rstrip())))

bfs(maze, visited)