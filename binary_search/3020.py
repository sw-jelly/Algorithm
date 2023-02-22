# 백준 3020번 : 개똥벌레
import sys
input = sys.stdin.readline

n, h = map(int, input().split())
a = []
b = []
for _ in range(n//2):
  a.append(int(input()))
  b.append(int(input()))

a.sort()
b.sort()
hei = [0 for _ in range(h)]
ta, tb = 0, 0
for i in range(n//2):
  aa, bb = a[i], b[i]

  for j in range(ta, aa):
    hei[j] += n//2 - i
  for j in range(tb, bb):
    hei[h-j-1] += n//2 - i

  ta, tb = aa, bb

hei.sort()
r1 = hei[0]
r2 = 0

for k in hei:
  if k == r1:
    r2 += 1
  else:
    break

print(r1, r2)