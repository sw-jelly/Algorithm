# 백준 1238번 : 파티
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(k, dist, g):
  q = []
  heapq.heappush(q, (0, k))
  dist[k] = 0

  while q:
    d, now = heapq.heappop(q)

    if dist[now] < d:
      continue

    for i in g[now]:
      cost = d + i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return dist

n, m, k = map(int, input().split())
g1 = [[] for _ in range(n+1)]
g2 = [[] for _ in range(n+1)]
dist1 = [INF] * (n+1)
dist2 = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  g1[a].append((b, c))
  g2[b].append((a, c))

d1 = dijkstra(k, dist1, g1)
d2 = dijkstra(k, dist2, g2)

result = 0
for i in range(1, n+1):
  if result < d1[i] + d2[i]:
    result = d1[i] + d2[i]

print(result)