# 백준 16236번 : 아기 상어
# BFS에 대한 풀이 참조 (백준 14940)
# [출처] https://dalseoin.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-14940-%EC%89%AC%EC%9A%B4-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC
from collections import deque
import sys

def bfs(x, y):
  q = deque() 
  q.append((x, y)) 
  visited[x][y] = 0
  
  while q:
    i, j = q.popleft()

    for k in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
      ni, nj = i + k[0], j + k[1]
      if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1:
        if s[ni][nj] == 0:
          visited[ni][nj] = visited[i][j] + 1
          q.append((ni, nj))
        elif s[ni][nj] == -2:
          visited[ni][nj] = -2


sharkLV = 2 # 상어 초기 값
result = 0 # 걸린 시간
count = 0 # 먹은 물고기 수
fishes = [] # 물고기들의 레벨, 위치 정보
space = [] # 공간 지도
helpMom = False # 게임 오버 여부

n = int(input())
for i in range(n):
  space.append(list(map(int, sys.stdin.readline().split())))

# 상어 및 물고기들의 위치 정보 저장
for i in range(n):
  for j in range(n):
    if space[i][j] == 9:
      sharkLoc = [i, j]
    elif space[i][j] != 0:
      fishes.append([space[i][j], i, j])

while helpMom != True:
  # 먹을 수 있는 물고기가 있는지
  helpMom = True
  avail = []
  s = [[0] * n for _ in range(n)]
  for i in range(len(fishes)):
    # 레벨이 낮으면 먹을 수 있다.
    if fishes[i][0] < sharkLV:
      helpMom = False
      avail.append(fishes[i])
    elif fishes[i][0] > sharkLV:
      s[fishes[i][1]][fishes[i][2]] = -2
      
  if helpMom:
    break
  else:
    visited = [[-1] * n for _ in range(n)]
    x, y = sharkLoc[0], sharkLoc[1]
    bfs(x, y)
    min = 999
    
    for f in avail: # 가장 가까운 곳 찾기
      if visited[f[1]][f[2]] > 0 and visited[f[1]][f[2]] < min:
        min = visited[f[1]][f[2]]
        minF = f
    
    if min == 999:  # 갈 수 있는 곳이 없다
      helpMom = True
    else: # 상어 이동, 정보 업데이트
      sharkLoc = [minF[1], minF[2]]
      fishes.remove(minF)
      result += min
      count += 1
    
    # 아기 상어 레벨 업
    if count == sharkLV:
      sharkLV += 1;
      count = 0
    
print(result)