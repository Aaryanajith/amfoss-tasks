(n,m)=map(int,input().split())

a=m%n
b=m/n


if m%n!=0:# to check whether if it is possible to reach target amount
    print("-1")
elif b==1:
    print("0")
    
elif n>m:
    print("-1")

elif a==0 and (b%2==0 or b%3==0):
    n=0
    while b!=1:
        if b%3==0:
            b=b/1
            n=n+1
        else:
            b=b/2
            n=n+1
    print(n)        