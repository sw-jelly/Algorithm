# 백준 1806번 : 부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
i, j = 0, 0
sum, tmp, r = nums[0], 1, 0

while i < n and j < n:
  #print(i, j, sum, tmp, r)
  if sum >= s:
    if not r or r > tmp:
      r = tmp
      
    if i < j:
      i += 1
      sum -= nums[i-1]
      tmp -= 1
    elif j+1 < n:
      j += 1
      sum += nums[j]
      tmp += 1
    else:
      break

  else:
    if j+1 < n:
      j += 1
      sum += nums[j]
      tmp += 1
      
    elif i+1 < n:
      i += 1
      sum -= nums[i-1]
      tmp -= 1
      
    else:
      break

print(r)