def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=" ")

  for i in range(len(graph[v])):
    if not visited[graph[v][i]]:
      dfs(graph, graph[v][i], visited)

graph = [[], 
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
        ]
visited = [False]*9

dfs(graph, 1, visited)