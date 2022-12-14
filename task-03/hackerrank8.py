n= int(input())
num=n
nstr=str(n)

count=0
flag=True
countdig=0
if len(str(n)) < 2:
    print(0)
    
else:
    while True:
        sumdig=0
        for i in str(n):
            sumdig=sumdig+int(i)
            
        count=count+1
        n=sumdig
        if len(str(n))==1:
            print(count)
            break