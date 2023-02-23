# 백준 1152번 : 단어의 개수
import sys
input = sys.stdin.readline

s = list(map(str, input().split()))
r = []
for k in s:
  if k != ' ':
    r.append(k)

print(len(r))