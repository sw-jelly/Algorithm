# 백준 2577번 : 숫자의 개수
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

l = list(map(int, str(a*b*c).rstrip()))
l.sort()

r = [0 for _ in range(10)]
k = 0
for n in l:
  if n == k:
    r[k] += 1
  else:
    k = n
    r[k] += 1

for n in r:
  print(n)