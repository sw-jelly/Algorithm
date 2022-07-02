# 백준 2839번 : 설탕 배달
n = int(input())
printed = False

if (n % 5) % 3 > 0:
  for i in range(3, 15, 3):
    if n - i > 0 and (n-i) % 5 == 0: # 5의 배수 + 3, 6, 9, 12
      print(int((n-i) / 5) + int(i/3))
      printed = True
      
  if printed == False:
    if n % 3 == 0: # only 3의 배수
      print(int(n / 3))
    else: # impossible
      print(-1)
      
else: # 5의 배수 + 3
  print(int(n / 5) + int((n % 5) / 3))