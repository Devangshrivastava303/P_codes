from collections import deque
def sameclassnotsit(n,m,a,b):
    adj=[[] for _ in range(n+1)]
    for i in range(m):
        x=a[i]
        y=b[i]
        adj[x].append(y)
        adj[y].append(x)
    visited=[False]*(n+1)
    max_persons=0
    for i in range(1,n+1):
        if not visited[i]:
            q=deque([i])
            visited[i]=True
            group_size=0
            while q:
                Curr=q.popleft()
                group_size+=1
                for bw in adj[Curr]:
                    if not visited[bw]:
                     visited[bw]=True
                     q.append(bw)
            max_persons=max(max_persons,group_size)
    print(max_persons)
sameclassnotsit(5,3,[2,1,3],[1,5,4])       
