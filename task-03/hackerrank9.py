n=int(input())
for i in range(n):
    no_keys=int(input())
    x,y,z=map(int, input().split())    
    xyz= str(x)+str(y)+str(z)
    
    if x==1 or y==2 or z==3:
        print("NO")
    else:
        if ("1" not in xyz) and xyz[0]=="0":
            print("NO")
        elif("2" not in xyz) and xyz[1]=="0":
            print("NO")
        elif("3" not in xyz) and xyz[2]=="0":
            print("NO")
        else:
            print("YES")