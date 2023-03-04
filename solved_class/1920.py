# 백준 1920번 : 수 찾기
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
mum = list(map(int, input().split()))

num.sort()
for k in mum:
  start, end = 0, n-1
  pf = False
  while start <= end:
    mid = (start+end)//2
    if num[mid] == k:
      pf = True
      break
    elif num[mid] > k:
      end = mid - 1
    else:
      start = mid + 1

  if pf:
    print(1)
  else:
    print(0)