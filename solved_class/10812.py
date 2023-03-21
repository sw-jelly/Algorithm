# 백준 10812번 : 바구니 순서 바꾸기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [i for i in range(n+1)]

for _ in range(m):
  a, b, k = map(int, input().split())
  basket[a:b+1] = basket[k:b+1] + basket[a:k]

for k in basket[1:]:
  print(k, end = ' ')
print()