def Factorial(n):
    if n==0:
        return 1
    else:
      return n*Factorial(n-1)




value=Factorial(5)
print(value)