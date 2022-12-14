t=int(input())
for i in range(t):
    n=int(input())
    water=list(input().split())
    
    ls=[]
    s=0
    
    for i in range(len(water)):
        if water[i]!="0":
            ind=i
            break
        
    for j in range(ind, len(water)-1):
        ls.append(water[j])
        
    for j in ls:
        s=s+int(j)
        
    print(s+ls.count('0'))
        