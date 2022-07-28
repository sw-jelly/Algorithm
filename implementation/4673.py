# 백준 4673번 : 셀프 넘버

l = 10000
selfNum = [i for i in range(1, 10000)]

i = 1
while i < l:
  # 각 자리 수 더하기
  num = i % 10
  k = i-num
  j = 100
  while k > 0:
    num += (k % j) / (j//10)
    k -= k % j
    j *= 10

  # 셀프 넘버가 아닌 수 빼기
  try:
    selfNum.remove(num+i)
  except ValueError:
    pass
    
  i += 1

for value in selfNum:
  print(value)