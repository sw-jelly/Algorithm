# 백준 2675번 : 문자열 반복
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  k, s = map(str, input().split())
  k = int(k)
  s = list(map(str, s.rstrip()))
  
  for i in range(len(s)):
    print(s[i]*k, end='')
  print()