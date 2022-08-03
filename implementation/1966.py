# 백준 1966번 : 프린터 큐
import sys

n = int(input())
result = []

for i in range(n):
  k, index = map(int, sys.stdin.readline().split())
  docs = list(map(int, sys.stdin.readline().split()))
  # 해당 인덱스의 우선순위를 실수로 만들기
  docs[index] = docs[index]/1.0

  count = 1
  while len(docs) > 0:
    # 최대값 구하기
    max = 0
    for j in range(len(docs)):
      if max < docs[j]:
        max = docs[j]

    j , k = 0, 0
    while k < len(docs):
      if docs[j] == max:
        break
      elif docs[j] < max:
        docs.append(docs[j])
        del docs[j]
        j -= 1
      j += 1
      k += 1

    # 실수인 값(해당 문서)을 제거할 때, count 값 저장
    if type(docs[0]) is float:
      result.append(count)
      break

    del docs[0]
    count += 1
      
for value in result:
  print(value)