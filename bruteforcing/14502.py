# 백준 14502번 : 연구소
import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(graph, visited, xx, yy):
  di = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  visited[xx][yy] = True
  q = deque([(xx, yy)])

  while q:
    x, y = q.popleft()
    
    for d in di:
      nx, ny = x+d[0], y+d[1]
      if 0 <= nx < n and 0 <= ny < m:
        if not graph[nx][ny] == 1 and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = True


n, m = map(int, input().split())
lab, virus, w = [], [], []

for i in range(n):
  li = list(map(int, input().split()))
  lab.append(li)

  for j in range(m):
    if li[j] == 2:
      virus.append((i, j))
    elif li[j] == 1:
      w.append((i, j))

w1 = []
for i in range(n):
  for j in range(m):
    w1.append((i, j))
    
walls = list(combinations(w1, 3))

result = 0
visited = [[False for _ in range(m)] for _ in range(n)]
for k in w:
  visited[k[0]][k[1]] = True

for wall in walls:
  x1, y1, x2, y2, x3, y3 = wall[0][0], wall[0][1], wall[1][0], wall[1][1], wall[2][0], wall[2][1]

  if not lab[x1][y1] and not lab[x2][y2] and not lab[x3][y3]:
    lab2 = copy.deepcopy(lab)
    lab2[x1][y1], lab2[x2][y2], lab2[x3][y3] = 1, 1, 1
    
    visited2 = copy.deepcopy(visited)
    visited2[x1][y1], visited2[x2][y2], visited2[x3][y3] = True, True, True
    
    for v in virus:
      bfs(lab2, visited2, v[0], v[1])

    tmp = 0
    for visit in visited2:
      tmp += visit.count(False)
    if tmp > result:
      result = tmp

print(result)