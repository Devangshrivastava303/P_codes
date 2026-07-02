def popcount(n):
    popcount=0
    for i in range(n+1):
        for j in range(n+1):
            pair= n[i]*n[j]
            if pair == n:
                n[i]%2,n[j]%2
                if n[i]==1:
                    popcount+=1
                else:
                    break
    return popcount
