# 백준 2108번 : 통계학
n = int(input())
a = []
count = [[0, -i] for i in range(-4000, 4001)]
sum = 0
for _ in range(n):
  k = int(input())
  a.append(k)
  count[k+4000][0] += 1
  sum += k
  
a.sort()
# 산술 평균
k = sum/n
if int(k) % 2 and k - int(k) == 0.5:
  print(round(k) + int(k/abs(k)))
else:
  print(round(k))

# 중앙값
print(a[n//2])

# 최빈값
count = count[(a[0]+4000):(a[n-1]+4001)]
count.sort()
len = len(count)
if len > 1 and count[len-1][0] == count[len-2][0]:
  print(-count[len-2][1])
else:
  print(-count[len-1][1])

# 범위
if n == 1:
  print(0)
else:
  print(a[n-1] - a[0])