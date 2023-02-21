# 백준 2470번 : 두 용액
# 이진 탐색 ver
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

def bs(k, a, start, end):
  mid = (start + end) // 2

  if a[mid] == k:
    return mid

  elif a[mid] > k:
    if (start > mid-1) or (mid > 0 and a[mid] - k < abs(a[mid-1] - k)):
      return mid
    return bs(k, a, start, mid-1)

  else:
    if (mid+1 > end) or (mid < len(a)-1 and k - a[mid] < abs(k - a[mid+1])):
      return mid
    return bs(k, a, mid+1, end)

a = []
b = []
for k in l:
  if k >= 0:
    a.append(k)
  else:
    b.append(k)
a.sort()
b.sort(reverse=True)

result = 2000000000
k1, k2 = n, n
if len(a) >= 2:
  k1, k2 = a[0], a[1]
  result = k1 + k2
if len(b) >= 2:
  if result + b[0] + b[1] >= 0:
    k1, k2 = b[1], b[0]
    result = k1 + k2

if a:
  tmpx = 0
  for k in b:
    tmpx = bs(-k, a, tmpx, len(a)-1)
    tmp = a[tmpx]
    if k + tmp == 0:
      k1, k2 = k, tmp
      break
    elif abs(k + tmp) < abs(result):
      result = k + tmp
      k1, k2 = k, tmp

if k1 > k2:
  k1, k2 = k2, k1
print(k1, k2)