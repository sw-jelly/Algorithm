# 백준 2389번 : 설탕 배달 (dp로 풀기)
import sys
sys.setrecursionlimit(10000)

n = int(input())
memory = [0 for _ in range(n+1)]

def dp(x):
  if x < 2:
    return -1
  if memory[x]:
    return memory[x]
  if not x % 5:
    return x//5
  if not x % 3:
    if x < 15:
      return x//3

  memory[x] = min(dp(x-5) + 1, dp(x-3) + 1)
  ans = memory[x] - 1
  if ans == -1:
    return -1
  else:
    return ans + 1


print(dp(n))
