# 백준 10803번 : 정사각형 만들기
# 풀이 참조함 [출처] https://chocochip101.tistory.com/entry/%EB%B0%B1%EC%A4%80-10803%EB%B2%88-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EB%A7%8C%EB%93%A4%EA%B8%B0-C-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%92%80%EC%9D%B4
# 왜 짧은 변 * 3 보다 긴 변이 길면 짧은 변을 한 변으로 한 정사각형을 만들어야 할까? 모르겠다...

import sys
sys.setrecursionlimit(10000)  
input = sys.stdin.readline

n, m = map(int, input().split())
if n < m:
  n, m = m, n
memory = [[0 for _ in range(m+1)] for _ in range(n+1)]

def dp(x, y): # dp(긴 변, 짧은 변)
  # 정사각형
  if x == y:
    return 1
    
  # 긴 변, 짧은 변 설정
  if x < y:
    x, y = y, x
    
  # 구해 놓은 값이 있다면
  if memory[x][y]:
    return memory[x][y]
    
  # 긴 변이 짧은 변의 배수
  if x % y == 0:
    return x//y

  # 긴 변이 짧은 변의 3배보다 길다면
  # 짧은 변을 한 변으로 한 정사각형 만들기
  if x >= y*3:
    memory[x][y] = dp(x-y, y) + 1
    return memory[x][y]

  min = 9999999
  # 긴 변 자르기
  for i in range(1, int(x/2)+1):
    tmp = dp(i, y) + dp(x-i, y)
    if min > tmp:
      min = tmp
    
  # 짧은 변 자르기
  for i in range(1, int(y/2)+1):
    tmp = dp(x, i) + dp(x, y-i)
    if min > tmp:
      min = tmp

  memory[x][y] = min
  return min

print(dp(n, m))