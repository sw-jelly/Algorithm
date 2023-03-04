# 백준 9012번 : 괄호
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  s = map(str, input().rstrip())
  sum = 0
  result = True
  
  for k in s:
    if k == "(":
      sum += 1
    elif k == ")":
      if sum:
        sum -= 1
      else:
        result = False
        break
        
  if sum:
    result = False
  
  if result:
    print("YES")
  else:
    print("NO")