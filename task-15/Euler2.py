def fib(n):
  fib = 0
  a, b = 0, 1
  while b <= n:
    if b % 2 == 0:
      fib += b
    a, b = b, a + b
  return fib


t=int(input("Test Case"))
for i in range(t):
      n=int(input("No of Elements"))
      result = fib(n)
      print(result)



        
       
    
        
            
        