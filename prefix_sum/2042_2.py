# 백준 2042번 : 구간 합 구하기 (펜윅트리 ver.)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
list = [0]
tree = [0] * (n+1)
for _ in range(n):
  list.append(int(input()))

def update(idx, value):
  while idx <= n:
    tree[idx] += value
    idx += idx & (~idx + 1)

def make():
  for i in range(1, n+1):
    update(i, list[i])

def sum(idx):
  r = 0
  while idx > 0:
    r += tree[idx]
    idx -= idx & (~idx + 1)
  return r

make()
for _ in range(m+k):
  a, b, c = map(int, input().split())
  if a == 1:
    update(b, c-list[b])
    list[b] = c
  elif a == 2:
    print(sum(c)-sum(b-1))