# 백준 2003번 : 수들의 합 2
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))

i, j = 0, 0
sum = s[i]
r = 0

while i < n and j < n:
  if sum > m:
    i += 1
    if i < n:
      sum -= s[i-1]
      
  elif sum == m:
    r += 1
    i += 1
    j += 1
    if j < n:
      sum -= s[i-1]
      sum += s[j]
      
  else:
    j += 1
    if j < n:
      sum += s[j]

print(r)