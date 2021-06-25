def towerofhanoi(n,s,d,a):
    if (n==1):
        print("Move disk 1 from rod ",s,"to rod",d)
        return
    towerofhanoi(n-1,s,a,d)
    print("Move disk",n," from rod",s,"to rod",d)
    towerofhanoi(n-1,a,d,s)

towerofhanoi(4,"A","C","B")
