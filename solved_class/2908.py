# 백준 2908번 : 상수
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a1 = a//100 + ((a%100)//10)*10 + (a%10)*100
b1 = b//100 + ((b%100)//10)*10 + (b%10)*100

print(max(a1, b1))