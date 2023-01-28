# 백준 12865번 : 평범한 배낭
# 해설 참조함 [출처 : https://chanhuiseok.github.io/posts/improve-6/]
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
th = [[0, 0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
  th.append(list(map(int, input().split())))

for i in range(1, n+1):
  for j in range(1, k+1):
    w, v = th[i][0], th[i][1]
    if w <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    else:
      dp[i][j] = dp[i-1][j]


print(dp[n][k])