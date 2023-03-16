# 백준 12015번 : 가장 긴 증가하는 부분 수열 2
import sys
input = sys.stdin.readline

def bin_search(k, lis):
  start = 0
  end = len(lis)-1
  while start <= end:
    mid = (start + end)//2
    if k == lis[mid]:
      return mid
    if k > lis[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return start

n = int(input())
s = list(map(int, input().split()))
lis = [s[0]]

for k in s:
  if k > lis[len(lis)-1]:
    lis.append(k)
  else:
    lis[bin_search(k, lis)] = k

print(len(lis))