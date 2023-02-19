# 백준 13334번 : 철로
# 풀이 참조함 - [출처] https://yongjoonseo.dev/problem%20solving/python/PS-baekjoon037/

import sys
import heapq
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
  a, b = map(int, input().split())
  if a > b:
    a, b = b, a
  l.append([a, b])
d = int(input())

l.sort(reverse=True)

hq = []
r = 0

for i in range(n):
  start, end = l[i][0], l[i][1]
  
  if end - start > d:
    continue

  heapq.heappush(hq, -end)
  
  while hq and -hq[0] > start + d:
    heapq.heappop(hq)

  r = max(r, len(hq))

print(r)