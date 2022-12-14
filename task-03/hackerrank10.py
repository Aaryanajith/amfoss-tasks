city=int(input("E5"))
lvl=list(input().split())
no_cars=0
no_groups=0
l=[]
        
for i in lvl:
    l.append(int(i))
l.sort()
while True:
    if len(l)==0:
        break
    
    for j in l:
        no_groups=no_groups+j
        l.remove(j)
        
        if no_groups>4:
            l.append(j)
            l.sort()
            no_groups=0
            no_cars+=1
            break
        if no_groups==3:
            l.sort()
            no_cars+=1
            no_groups=0
            break
        if no_groups==4:
            l.sort()
            no_cars+=1
            no_groups=0
            break
        elif no_groups<4 :
            break
print(no_cars)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        