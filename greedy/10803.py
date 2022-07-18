# 백준 10803번 : 정사각형 만들기
# 해결 안됨...
import sys

n, m = map(int, sys.stdin.readline().split())
squares = [[n, m]]
result = 0

if n == m: # 입력이 정사각형일 때
  result = 0
  
else:
  while squares:
    print(squares)
    
    if squares[0][0] == squares[0][1]: # 정사각형일 때
      del squares[0]
      result += 1
  
    else:
      if squares[0][0] > squares[0][1]:
        long, short = squares[0][0], squares[0][1]
      else:
        long, short = squares[0][1], squares[0][0]
        
      # 한 변의 길이가 1일 때
      if short == 1:
        result += long
        del squares[0]

      # 긴 변이 짧은 변의 배수인 경우
      elif long % short == 0:
        result += long//short
        del squares[0]

      # 직사각형으로 2등분
      # elif long % 2 == 0 and short % 2 == 1 and long % ((short//2)+1) == 0: 
      #   squares.append([short//2,long])
      #   squares.append([short-short//2, long])
      #   del squares[0]

      elif long % 2 == 0 and short - long//2 > 1:
        squares.append([long//2,long])
        squares.append([short-(long//2), long])
        del squares[0]

      elif long % 3 == 0 and short - long//3 > 1:
        squares.append([long//3,long])
        squares.append([short-(long//3), long])
        del squares[0]
        
      elif short % 2 == 0:
        squares.append([short//2,short])
        squares.append([long-(short//2),short])
        del squares[0]

      elif short % 3 == 0:
        squares.append([short//3,short])
        squares.append([long-(short//3),short])
        del squares[0]
          
      else: # 나머지 경우 -> 작은 변을 한 변으로 큰 정사각형 만들기
        squares.append([long-short, short])
        squares.append([short,short])
        del squares[0]
    
print(result)