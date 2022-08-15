# 백준 10026번 : 적록 색약
import copy
from collections import deque

def numOfRegions(image):
  visited = [[False] * n for _ in range(n)]
  q = deque([[0, 0]])
  visited[0][0] = True
  # 방향 : 우, 하, 좌, 상
  directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  num = 0

  while q:
    i, j = q[0][0], q[0][1]
    q.popleft()
    c = image[i][j]

    for d in directions:
      ni, nj = i+d[0], j+d[1]
      if 0 <= ni < n and 0 <= nj < n:
        if image[ni][nj] == c and visited[ni][nj] == False:
          q.append([ni, nj])
          visited[ni][nj] = True
      
    if not q:
      num += 1
      for i in range(n):
        for j in range(n):
          if visited[i][j] == False:
            q.append([i, j])
            visited[i][j] = True
            break
        if q:
          break
 
  return num

# 입력 받기
image = []
n = int(input())
for i in range(n):
  image.append(list(input()))

# 적록색맹 이미지 : 본래 이미지의 초록색을 빨간색으로 변환하기
image_colorBlind = copy.deepcopy(image)

for i in range(n):
  for j in range(n):
    if image_colorBlind[i][j] == 'G':
      image_colorBlind[i][j] = 'R'

print(numOfRegions(image), numOfRegions(image_colorBlind))