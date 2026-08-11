def taxi():
    n=int(input())
    s=list(map(int,input().split()))
    k=4
    cabs=0
    count=[0]*5
    for num in s:
        count[num]+=1
    cabs+=count[4]
    cabs+=count[3]
    count[1]=max(0,count[1]-count[3])
    cabs += count[2] // 2                    
    if count[2] % 2 == 1:
        cabs += 1                             
        count[1] = max(0, count[1] - 2)      
    cabs += (count[1] + k - 1) // k           
    print(cabs)
taxi()