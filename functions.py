def factorial(num): 
    "Calculate Factorial number"
   if num == 1: 
     return 1 
   return (factorial(num - 1) * num) 
   
def fib(n):    # write Fibonacci series up to n
     "Print a Fibonacci series up to n"
     a, b = 0, 1
     while b < n:
         print b,
         a, b = b, a+b
         
        
