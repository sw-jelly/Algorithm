# 백준 2170번 : 선 긋기
import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
  l.append(list(map(int, input().split())))

l.sort()
r, a, b = 0, l[0][0], l[0][1]
  
for i in range(1, len(l)):
  # 선 새로 시작
  if l[i][0] > b:
    r += b - a
    a, b = l[i][0], l[i][1]
    
  # 선이 일부 겹침
  elif l[i][0] <= b and l[i][1] > b:
    b = l[i][1]

r += b - a
print(r)