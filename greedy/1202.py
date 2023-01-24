# 백준 1202번 : 보석 도둑
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
max = 300000

jw = []
bag = []
for _ in range(n):
  heapq.heappush(jw, list(map(int, input().split())))
for _ in range(k):
  bag.append(int(input()))

bag.sort()
r = 0

jew = []

for b in bag:
  for i in range(len(jw)):
    if jw[0][0] <= b:
      heapq.heappush(jew, max - heapq.heappop(jw)[1])
    else:
      break
      
  if not jew:
    continue
  r += max - heapq.heappop(jew)

print(r) 