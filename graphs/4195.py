# 백준 4195번 : 친구 네트워크
# 풀이 참조함 
# [출처] https://reliablecho-programming.tistory.com/81
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(f, x):
  if f[x] != x:
    f[x] = find(f, f[x])
  return f[x]

def union(f, a, b):
  a = find(f, a)
  b = find(f, b)

  if a != b:
    f[b] = a
    c[a] += c[b]
  print(c[a])

m = int(input())
for i in range(m):
  f = dict() # "user" : "parent"
  c = dict() # "user" : "# in friends network"
  n = int(input())
  for _ in range(n):
    a, b = map(str, input().split())
    if not a in f:
      f[a] = a
      c[a] = 1
    if not b in f:
      f[b] = b
      c[b] = 1

    union(f, a, b)