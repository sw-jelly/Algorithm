# 백준 14002번 : 가장 긴 증가하는 부분 수열 4
def bin_search(k, lis):
  start = 0
  end = len(lis) - 1
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
index = [0] * n

for i in range(n):
  k = s[i]
  if k > lis[len(lis)-1]:
    index[i] = len(lis)+1
    lis.append(k)
  else:
    ii = bin_search(k, lis)
    lis[ii] = k
    index[i] = ii+1

r = len(lis)
print(r)

result = []
for i in range(n-1, -1, -1):
  if index[i] == r:
    result.append(s[i])
    r -= 1
  if r < 0:
    break

result.reverse()
for k in result:
  print(k, end=' ')
print()