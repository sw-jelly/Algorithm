# 백준 9466번 : 텀 프로젝트
# 시간 초과 관련 풀이 참고
# [출처] https://claude-u.tistory.com/435

def areWeTeam(j, s, visited, q):
  visited[j] = True
  q.append(j)
  if visited[s[j]] == True:
    for k in range(len(q)):
      if s[j] == q[k]:
        for m in range(k, len(q)):
          result.append(1)
    return
  areWeTeam(s[j], s, visited, q)

import sys
sys.setrecursionlimit(10**6)

t = int(input())

for i in range(t):
  n = int(input())
  s = list(map(int, sys.stdin.readline().split()))
  s.insert(0, 0)
  visited = [False] * (n + 1)
  visited[0] = True
  result = []

  # 팀 구하기
  for j in range(n + 1):
    if visited[j] == False:
      q = []
      areWeTeam(j, s, visited, q)

  # 팀을 이루지 못한 사람 수 구하기
  print(n - len(result))