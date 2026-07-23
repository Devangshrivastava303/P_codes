def feelingproud():
    n=int(input())
    def kamtareeke(n):
        if n==1:
            return 0
        ektareeka=1+kamtareeke(n-1)
        duatareeka=1+kamtareeke(n-n//2)
        tisratareeka=1+kamtareeke(n-(2*n)//3) if n>=3 else float('inf')

        return min(ektareeka,duatareeka,tisratareeka)
    print(kamtareeke(n))
feelingproud()