# 백준 11053번 : 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
mm = [0 for _ in range(n)]

def dp(x):
  if x == len(num):
    return
  if mm[x]:
    return mm[x]

  max = 0
  for i in range(x+1, len(num)):
    if num[x] < num[i]:
      tmp = 1 + dp(i)
      if tmp > max:
        max = tmp
        
  # 증가하는 부분이 있다
  if max:
    mm[x] = max
  # 증가하는 부분이 없다
  else:
    mm[x] = 1
    
  return mm[x]

for k in range(n):
  dp(k)

mm.sort(reverse = True)
print(mm[0])