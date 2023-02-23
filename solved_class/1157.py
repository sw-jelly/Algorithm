# 백준 1157번 : 단어 공부
import sys
input = sys.stdin.readline

s = list(map(str, input().rstrip().upper()))
s.sort()

r = [[1, s[0]]]
tmp = s[0]
k = 0
for i in range(1, len(s)):
  if s[i] == r[k][1]:
    r[k][0] += 1
  else:
    r.append([1, s[i]])
    k += 1

r.sort(reverse=True)
if len(r) > 1 and r[0][0] == r[1][0]:
  print('?')
else:
  print(r[0][1])