# 백준 1717번 : 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_parents(p, x):
  if p[x] != x:
    p[x] = find_parents(p, p[x])
  return p[x]

def union_parents(p, a, b):
  a = find_parents(p, a)
  b = find_parents(p, b)
  if a < b:
    p[b] = a
  else:
    p[a] = b

n, m = map(int, input().split())
p = [i for i in range(n+1)]

for _ in range(m):
  k, a, b = map(int, input().split())
  if k == 0: # 합집합
    union_parents(p, a, b)
    
  elif k == 1: # 같은 집합인가?
    if find_parents(p, a) == find_parents(p, b):
      print("YES")
    else:
      print("NO")