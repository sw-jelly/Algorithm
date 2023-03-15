# 백준 22856번 : 트리 순회
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)
visited[0] = True

for _ in range(n):
  a, b, c = map(int, input().split())
  graph[a].append(b)
  graph[a].append(c)
  if not b == -1:
    parent[b] = a
  if not c == -1:
    parent[c] = a

s = []
def inorder(x):
  if graph[x][0] != -1:
    inorder(graph[x][0])
  s.append(x)
  if graph[x][1] != -1:
    inorder(graph[x][1])

inorder(1)
last = s[n-1]
r, x = 0, 1
while True:
  r += 1
  visited[x] = True

  left, right = graph[x][0], graph[x][1]
  if left != -1 and not visited[left]:
    x = left
  elif right != -1 and not visited[right]:
    x = right
  elif x == last:
    print(r-1)
    break
  elif parent[x]:
    x = parent[x]