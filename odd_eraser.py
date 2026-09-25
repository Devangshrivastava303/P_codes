import math
def odd_eraser():
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split())) 
        if n==1:
            print(arr[0])
            continue
        while len(arr)>2:
            arr.pop(1)
        print(math.gcd(arr[0],arr[1]))
odd_eraser()    