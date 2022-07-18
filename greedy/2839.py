# 백준 2839번 : 설탕 배달
n = int(input())
printed = False

# 5의 배수 & 5의 배수 + 3, 6, 9, 12
for i in range(0, 15, 3):
  if n-i > 0 and (n-i) % 5 == 0: # 5의 배수 + 0, 3, 6, 9, 12
    print(((n-i)//5) + (i//3))
    printed = True

if printed == False:
  if n % 3 == 0: # only 3의 배수
    print(n//3)
  else: # impossible
    print(-1)