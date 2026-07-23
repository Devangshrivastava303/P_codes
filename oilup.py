def oiltank():
    N=int(input())
    C=int(input())
    A = [int(input()) for _ in range(N)]
    kam_preshan=float('inf')
    maxi_X=0

    for valu in range(C+1):
        curr_l=valu
        distur=0

        for first_val in A:
            if first_val==1:
                if curr_l==C:
                    distur+=1
                else:
                    curr_l+=1
            elif first_val==-1:
                if curr_l==0:
                    distur+=1
                else:
                    curr_l-=1
        if distur<kam_preshan:
            kam_preshan=distur
            maxi_X=valu
    return maxi_X
print(oiltank())