# 백준 2805번 : 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))
t.sort(reverse=True)

start = 0
end = t[0]
while start <= end:
  mid = (start + end)//2
  sum = 0
  for i in range(n):
    sum += max(0, t[i]-mid)

  if sum >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)