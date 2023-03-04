# 백준 4949번 : 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
  s = []
  a = list(map(str, input().rstrip()))
  if len(a) == 1 and a[0] == ".":
    break
  for k in a:
    # 문장의 끝
    if k == ".":
      if s:
        print("no")
      else:
        print("yes")
      break

    # 괄호 열림
    if k == "(" or k == "[":
      s.append(k)
      
    # 괄호 닫힘
    elif k == ")":
      if s and s[len(s)-1] == "(":
        del s[len(s)-1]
      else:
        print("no")
        break
        
    elif k == "]":
      if s and s[len(s)-1] == "[":
        del s[len(s)-1]
      else:
        print("no")
        break