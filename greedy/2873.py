# 백준 2873번 : 롤러코스터
import sys

r, c = map(int, sys.stdin.readline().split())
min = 0
rX, rY = 0, 0
rc = []
rcHeap = []
result = ''

# 행 개수가 홀수일 때 : 모든 칸을 방문할 수 있음
if r % 2 != 0: 
  result = ('R'*(c-1) + 'D' + 'L'*(c-1) + 'D')*(r//2) + 'R'*(c-1)

# 열 개수가 홀수 일때 : 모든 칸을 방문할 수 있음
elif c % 2 != 0:
  result = ('D'*(r-1) + 'R' + 'U'*(r-1) + 'R')*(c//2) + 'D'*(r-1)

# 행, 열이 모두 짝수
else:
  # (짝수, 홀수) or (홀수, 짝수) 칸 하나 제외 모든 칸 방문 가능
  # 해당 칸이 최대한 작은 숫자가 될 수 있도록 하기
  
  for i in range(r):
    rc.append(list(map(int, sys.stdin.readline().split())))

  min = 1000
  for i in range(r):
    for j in range(c):
      if rc[i][j] < min and (i+j) % 2 != 0:
        rX, rY = i, j
        min = rc[i][j]

  if rX % 2 != 0: # (홀수, 짝수)
    if r > 2 and c > 2: # 행렬의 크기가 2*2 이상
      result = ('R'*(c-1) + 'D' + 'L'*(c-1) + 'D')*((rX-1)//2)
      
    if rY == 0: # 왼쪽 모서리 값 처리
      result += 'R' + 'D'
    else:
      result += ('D' + 'R' + 'U' + 'R')*(rY//2) + 'R' + 'D'

    if rY + 1 < c-1: # 가로 나머지 구간
      result += 'R' + 'U' + 'R' + ('D' + 'R' + 'U' + 'R')*((c-(rY+3))//2) + 'D'

    if rX + 1 < r-1: # 남은 구간
      result += 'D' + ('L'*(c-1) + 'D' + 'R'*(c-1) + 'D')*((r-(rX+2))//2) + 'L'*(c-1) + 'D' + 'R'*(c-1)
      

  else:  # (짝수, 홀수)
    if r > 2 and c > 2: # 행렬의 크기가 2*2 이상
      result = ('R'*(c-1) + 'D' + 'L'*(c-1) + 'D')*(rX//2)
    result += ('D' + 'R' + 'U' + 'R')*(rY//2) + 'D'
    
    if rY == c-1: # 오른쪽 모서리 값 처리
      result += 'R'
    else:
      result += 'R'*2 + 'U' + 'R' + ('D' + 'R' + 'U' + 'R')*((c-(rY+2))//2) + 'D'
    
    if rX + 1 < r-1: # 남은 구간
      result += 'D' + ('L'*(c-1) + 'D' + 'R'*(c-1) + 'D')*((r-(rX+3))//2) + 'L'*(c-1) + 'D' + 'R'*(c-1)
      
print(result)