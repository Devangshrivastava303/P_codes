def beauty():
    nums=list(map(int,input().split()))
    k=int(input())
    x=int(input())
    res=[]
    n=len(nums)
    i=0
    curr_wind=[]
    for r in range(0,n):
        curr_wind.append(nums[r])
        if len(curr_wind)==k:
            curr_wind.sort()
            xth=curr_wind[x-1]
            if xth<0:
                res.append(xth)
            else:
                res.append(0)
            curr_wind.remove(nums[i])
            i+=1
    print(*res)
beauty()