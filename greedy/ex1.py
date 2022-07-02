# [예제] 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
first = 0
second = 0
sum = 0

for i in range(0, n):
  if data[i] > second:
    if data[i] > first:
      first, second = second, first
      first = data[i]
    else:
      second = data[i]


while True:
  for i in range(0, k):
    if m > 0:
      sum += first
      m -= 1
    else:
      break
  if m > 0:
    sum += second
    m -= 1
  else:
    break

print(sum)
