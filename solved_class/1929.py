# 백준 1929번 : 소수 구하기
import sys
from math import sqrt
input = sys.stdin.readline

def prime(a, b, n):
  n[0], n[1] = 0, 0
  for i in range(2, int(sqrt(b))+1):
    if n[i] == 0:
      continue
    for j in range(i*2, b+1, i):
      n[j] = 0

  del n[:a]
  for k in n:
    if k:
      print(k)

a, b = map(int, input().split())
n = [i for i in range(b+1)]
prime(a, b, n)