# 백준 4195번 : 친구 네트워크
# [풀이 참조함] 출처 : 
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

  tf = False
  for i in range(len(a)):
    if a[i] < b[i]:
      f[b] = a
      tf = True
      break
    elif a[i] > b[i]:
      f[a] = b
      tf = True
      break

  # 두 문자열이 포함관계이면 짧은 쪽이 부모
  if not tf:
    f[b] = a

m = int(input())
for i in range(m):
  f = dict() # "user" : "parent"
  n = int(input())
  for _ in range(n):
    a, b = map(str, input().split())
    if not a in f:
      f[a] = a
    if not b in f:
      f[b] = b

    union(f, a, b)

    p = f[a]
    sum = 0
    for k in f:
      if find(f, k) == p:
        sum += 1
    print(sum)
    print(f)