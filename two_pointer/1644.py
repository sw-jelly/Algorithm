# 백준 1644번 : 소수의 연속합
# [풀이 참조] 소수 - 에라토스테네스의 체
n = int(input())
p = [True] * (n+1)
p[0], p[1] = False, False
r = 0

for i in range(2, n+1):
  if not p[i]:
    continue
  for j in range(i+i, n+1, i):
    p[j] = False

p = [i for i in range(2, n+1) if p[i]]
  
if n == 1:
  r = 0

else:
  i, j = 0, 0
  sum = 2
  #print(p)
  while i < len(p) and j < len(p):
    #print(i, j, sum)
    if sum == n:
      r += 1

    if sum >= n and i + 1 < len(p):
      i += 1
      sum -= p[i-1]
        
    elif sum < n and j + 1 < len(p):
      j += 1
      sum += p[j]

    else:
      break

print(r)