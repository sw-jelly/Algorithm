# 백준 1546번 : 평균
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
m = l[0]

sum = 0
for k in l:
  sum += k

# 점수/M*100
print(((sum/n)*10000)/(m*100))