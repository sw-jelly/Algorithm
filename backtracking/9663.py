# 백준 9663번 : N-Queen
n = int(input())
global result
result = 0

def dfs(v, s):
  global result
  if v == n:
    result += 1
    return

  for i in range(n):
      add = True
      for j in range(v):
        if s[j] == i or abs(j-v) == abs(s[j]-i):
          add = False
          break

        # for k in range(1, n):
        #   if s[j][0] - k == v or s[j][0] + k == v:
        #     if s[j][1] + k == i or s[j][1] - k == i:
        #       add = False
        #       break

      if add:
        # s.append([v, i])
        s[v] = i
        dfs(v+1, s)
        # s.pop()

s = [0 for _ in range(n)]
dfs(0, s)
print(result)