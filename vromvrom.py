# def remainingMethods(n,k,invocations):
#         ans=[]
#         for i in range(n):
#             if invocations[k][0] or invocations[k][1] == invocations[i][0] or invocations[i][1]:
#                 invocations.remove(invocations[i])
#                 print(invocations)
# remainingMethods(5,0,[[1,2],[0,2],[0,1],[3,4]])
def dfs(graph,start,visited):
    visited[start]
    for next_node in graph[start]:
        dfs(graph,next_node,visited)

graph={
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A']),
        'D': set(['B']),
        'E': set(['B']),
    }
visited=set()
dfs(graph,'A',visited)