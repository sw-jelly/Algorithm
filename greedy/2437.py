# 백준 2437번 : 저울
# 풀이 참조함 => https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hongjg3229&logNo=221627349685
import sys

n = int(input())
weights = list(map(int, sys.stdin.readline().split()))
sum = 0
i = 0

weights.sort()

# 작은 추부터 차례로 무게를 올려갈 때 올린 추의 무게 + 1 이 그 다음 추의 무게보다 작다면
# 올린 추의 무게 + 1의 무게를 구할 방법이 없으므로 최소 불가능한 무게가 누적합 + 1이 된다.

while True:
  # 모든 추를 더한 값 + 1
  if i == n:
    result = sum + 1
    break
  # 누적합 + 1 이 다음 추 무게보다 작은 경우 : 누적합 + 1
  elif sum + 1 < weights[i]:
    result = sum + 1
    break
  # 나머지 경우 : 다음 추를 누적합에 더해주기
  else:
    sum += weights[i]
    i += 1

print(result)