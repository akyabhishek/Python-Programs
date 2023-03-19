def test(N,M,C):
    sum=0
    for i in range(N):
        sum=sum+C[i]
    return sum%M
    

T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())
    C=list(map(int,input().split()))
    print("Case #",i,": ",test(N,M,C),sep="")