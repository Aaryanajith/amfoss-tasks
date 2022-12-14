def prime(n):
    i=2
    while n>1:
        if n % i == 0:
            n=n/i
        else:
            i+=1
    return i

t=int(input())
for i in range(t):
    n=int(input())
    print(prime(n))