# 백준 1018번 : 체스판 다시 칠하기
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
b = []

bw = 'BW'
wb = 'WB'

r1 = [[0 for _ in range(n-7)] for _ in range(m-7)]
r2 = [[0 for _ in range(n-7)] for _ in range(m-7)]

for _ in range(m):
  b.append(list(map(str, input().rstrip())))

for i in range(m-7):
  for j in range(n-7):
    for ij in range(i, i+8):
      for jj in range(j, j+8, 2):
        l = b[ij][jj] + b[ij][jj+1]
        if l == 'BB' or l == 'WW':
          r1[i][j] += 1
          r2[i][j] += 1
  
        elif l != bw:
          r1[i][j] += 2
  
        elif l != wb:
          r2[i][j] += 2
          
      bw, wb = wb, bw


for i in range(m-7):
  r1[i].sort()
  r2[i].sort()

r1.sort()
r2.sort()

if r1[0][0] < r2[0][0]:
  print(r1[0][0])
else:
  print(r2[0][0])