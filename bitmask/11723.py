# 백준 11723번 : 집합
# split으로 입력 받으면 해당 변수는 리스트가 됨
import sys
input = sys.stdin.readline

n = int(input())
s = 0

for _ in range(n):
  line = input().split()

  if line[0] == "all":
    s = (1 << 21) - 1
  elif line[0] == "empty":
    s = 0
  else:
    order, num = line[0], int(line[1])

    if order == "add":
      s |= (1 << (num-1))
    elif order == "remove":
      s &= ~(1 << (num-1))
    elif order == "check":
      if s & (1 << (num-1)):
        print(1)
      else:
        print(0)
    elif order == "toggle":
      s ^= (1 << (num-1))