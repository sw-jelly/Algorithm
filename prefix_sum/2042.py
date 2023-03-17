# 백준 2042번 : 구간 합 구하기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [0] * (n*4)
list = [0]
for _ in range(n):
  list.append(int(input()))

def make(node, start, end):
  if start == end:
    tree[node] = list[start]
    return tree[node]
    
  mid = (start + end)//2
  lr = make(node*2, start, mid)
  rr = make(node*2+1, mid+1, end)
  tree[node] = lr + rr
  return tree[node]

def sum(node, start, end, left, right):
  if start > right or end < left:
    return 0
  if start >= left and end <= right:
    return tree[node]

  mid = (start + end)//2
  lr = sum(node*2, start, mid, left, right)
  rr = sum(node*2+1, mid+1, end, left, right)
  return lr + rr

def update(node, start, end, index, diff):
  if index < start or index > end:
    return
  tree[node] += diff

  if start != end:
    mid = (start + end)//2
    update(node*2, start, mid, index, diff)
    update(node*2+1, mid+1, end, index, diff)

make(1, 1, n)
for _ in range(m+k):
  a, b, c = map(int, input().split())
  if a == 1:
    diff = c - list[b]
    list[b] = c
    update(1, 1, n, b, diff)
  elif a == 2:
    print(sum(1, 1, n, b, c))