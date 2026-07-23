def nintandqqueries():
    n=int(input())
    A=list(map(int,input().split()))
    q=int(input())
    queries=[] 
    for _ in range(q):
        queries.append(list(map(int,input().split())))
    result=0
    for query in queries:
        first_val=query[0]
        l=query[1]
        r=query[2]
        if first_val==1:
            Al=A[l]
            for i in range (l,r+1):
                A[i]=(i-l+1)*Al
        elif first_val==2:
            result+=sum(A[l:r+1])
    print(result)
    return result
nintandqqueries()
                

           
        
