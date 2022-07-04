# 백준 1715번 : 카드 정렬하기
# ★ for문, 순환 함수 이용시 시간 초과 -> 히프 이용하기

import heapq
result = 0
count = 0
n = int(input())
cards = []
for i in range (n):
  heapq.heappush(cards, int(input()))

if n == 1: # 카드 더미가 하나
  result = 0
else:
  while len(cards) > 1:
    count = heapq.heappop(cards)
    count += heapq.heappop(cards)

    result += count
    heapq.heappush(cards, count)
  
print(result)