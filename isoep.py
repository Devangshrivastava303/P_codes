def isoef(n,nums):
    for i in range(n):
        if nums[i]=='1':
            print("Hard")
            return
    print("Easy")

n = int(input())    
nums = input().split()

isoef(n, nums)