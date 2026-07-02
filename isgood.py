def isgood():
    x=int(input())
    count=0
    while(x>0):
        count+=1
        x//=10
    y=1
    for j in range(count):
        y*=10
    y+=1
    print(y)
isgood()
