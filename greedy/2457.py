# 백준 2457번 : 공주님의 정원
import sys
input = sys.stdin.readline

n = int(input())
f = []

for _ in range(n):
  f.append(list(map(int, input().split())))

a = [3, 1]
tmp = [0, 0]
tmpi = 0
r = 0

while a[0] < 12:
  ch = False
  for i in range(len(f)):
    if f[i][0] < a[0] or (f[i][0] == a[0] and f[i][1] <= a[1]):
      if tmp[0] < f[i][2] or (tmp[0] == f[i][2] and tmp[1] < f[i][3]):
        tmp = [f[i][2], f[i][3]]
        tmpi = i
        ch = True

  if ch:
    a = tmp
    del f[tmpi]
    r += 1
  else:
    r = 0
    break

print(r)