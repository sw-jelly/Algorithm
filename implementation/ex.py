# [예제] 게임 개발
import sys

n, m = map(int, sys.stdin.readline().split())
crntLoc = list(map(int, sys.stdin.readline().split()))
gameMap = []
for i in range(n):
  gameMap.append(list(map(int, sys.stdin.readline().split())))

move = [[-1, 0], [0, -1], [1, 0], [0, 1]]
result = 1
visited = [[0] * m for _ in range(n)]

visited[crntLoc[0]][crntLoc[1]] = 1
over = False
while True:
  x, y, d = crntLoc[0], crntLoc[1], crntLoc[2]
  direction = [(d+1)%4, (d+2)%4, (d+3)%4, d]

  for i in range(4):
    newX, newY = x+move[direction[i]][0], y+move[direction[i]][1]
    
    # 네 방향 모두 <가본 곳 or 바다가 있어서 못 감>
    if i == 3:
      if gameMap[newX][newY] == 1:
        over = True
        break
      else:
        crntLoc = [newX, newY, i]
      
    # 안 가본 육지가 있음
    elif gameMap[newX][newY] == 0 and visited[newX][newY] == 0:
      crntLoc = [newX, newY, direction[i]]
      visited[newX][newY] = 1
      result += 1
      break

  if over:
    break

print(result)