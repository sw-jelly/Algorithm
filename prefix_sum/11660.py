import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = []
s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
	l = list(map(int, input().split()))
	num.append(l)

for i in range(1, n + 1):
	for j in range(1, n + 1):
		s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + num[i-1][j-1]

for k in range(m):
	a, b, c, d = map(int, input().split())
	print(s[c][d] - s[a-1][d] - s[c][b-1] + s[a-1][b-1])
