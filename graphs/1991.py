# 백준 1991번 : 트리 순회
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

k = 65  #'A'
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
  a, b, c = map(str, input().split())
  graph[ord(a)-k].append(b)
  graph[ord(a)-k].append(c)

def preorder(x):
  print(chr(x+k), end="")
  if graph[x][0] != '.':
    preorder(ord(graph[x][0])-k)
  if graph[x][1] != '.':
    preorder(ord(graph[x][1])-k)

def inorder(x):
  if graph[x][0] != '.':
    inorder(ord(graph[x][0])-k)
  print(chr(x+k), end="")
  if graph[x][1] != '.':
    inorder(ord(graph[x][1])-k)

def postorder(x):
  if graph[x][0] != '.':
    postorder(ord(graph[x][0])-k)
  if graph[x][1] != '.':
    postorder(ord(graph[x][1])-k)
  print(chr(x+k), end="")

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()