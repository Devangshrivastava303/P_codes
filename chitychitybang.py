def cityAtoB():
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    costB=[]
    for i in range(len(A)):
        costB.append(min(A[i],B[i])+B[i])
    vibhag=[]
    for i in range(len(A)):
        vibhag.append((costB[i]-A[i],i))

    vibhag.sort(key=lambda x:x[0],reverse=True)
    total=0
    for i in range(N):
        idx=vibhag[i][1]
        total+=A[idx]
    for i in range(N,len(vibhag)):
        idx=vibhag[i][1]
        total+=costB[idx]
    print(total)
cityAtoB()

