# 백준 1654번 : 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cable = []
sum = 0
for _ in range(k):
  i = int(input())
  sum += i
  cable.append(i)

cable.sort(reverse=True)
start = 1
end = cable[0]
while start <= end:
  mid = (start+end)//2
  tmp = 0
  for c in cable:
    tmp += c//mid

  if tmp >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)