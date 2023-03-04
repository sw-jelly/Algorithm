# 백준 2164번 : 카드2
import math
n = int(input())
if n == 1:
  print(1)
else:
  for i in range(1, n):
    if n <= math.pow(2, i):
      print(int((n - math.pow(2, i-1)) * 2))
      break