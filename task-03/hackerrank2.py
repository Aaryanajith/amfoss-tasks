t=int(input())
for i in range(t):
    n=int(input())
    health=list(input().split())
    
    win=True
    
    for j in range(len(health)):
        if health[0]==health[1] and health[0]!='1': #checking health of monsters are equal and health not equal to 1
            win=False
            break
        
        if j==len(health) -1: #checking if j reached the last element
            break
        
        if int(health[j])>int(health[j+1]) and j==0: #checking if first monster's health is greatger than second monster
            win=False
            break
        
        else:
            continue
    
    if win==False:
        print('NO')
    else:
        print('YES')