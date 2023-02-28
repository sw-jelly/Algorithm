# 1874번 : 스택 수열
n = int(input())
l = []
a = [False for _ in range(n)]
for _ in range(n):
  l.append(int(input()))

p, end, min = 0, 0, n
r = ''
for i in range(n):
  k = l[i]
  if k > p:
    r += '+' * (k-p) + '-'
    a[p:k-1] = [True for _ in range(k-p-1)]
    p = k
  else:
    if i < n-1:
      if (k > l[i+1] or l[i+1] > p) and not a[k]:
        a[k-1] = False
        r += '-'
      else:
        break
    else:
      r += '-'

if len(r) == 2*n:
  for i in r:
    print(i)
else:
  print('NO')