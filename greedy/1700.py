# 백준 1700번 : 멀티탭 스케쥴링
import sys

n, k = map(int, sys.stdin.readline().split())
plugs = list(map(int, sys.stdin.readline().split()))
concent = []
count = 0

i = 0
while i < k:
  passed = False
  
  # 이미 꽂혀있다면 넘어간다.
  for j in range(len(concent)):
    if plugs[i] == concent[j]:
      passed = True
      break

  # 해당 플러그가 꽂혀있지 않은 경우
  if passed == False:
    # 빈 콘센트가 있다면 거기 꽂는다.
    if len(concent) < n:
      concent.append(plugs[i])
      
    # 빈 콘센트가 없는 경우
    else:
      # 아래 조건을 만족할 때까지 반복문을 돈 후 뺄 수 있는 콘센트를 뺀다.
      # 1. 해당 콘센트 뒤에 이미 꽂혀있는 콘센트가 (n-1)가지 나올 때
      # 2. 콘센트 배열 끝에 도달했을 때
      available = concent.copy() 
      
      j = i+1
      while len(available) > 1 and j < k:
        for m in range(n):
          if concent[m] == plugs[j]:
            try:
              available.remove(concent[m])
              break
            except ValueError:
              pass
        j += 1

      concent.remove(available[0])
      concent.append(plugs[i])
      count += 1
      
  i += 1
        
print(count)