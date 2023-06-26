a=int(input("Enter a number:"))
if a%2==0:
    b=str(a)
    c=b[::-1]
    d=int(c)
    if d==a:
        print(a,"is a palindrome.")
    else:
        print(a,"is not a palindrome.")
else:
    fact=1
    for i in range(a,0,-1):
        fact=fact*i
    print("Factorial of",a,"is",fact)
    z=str(fact)
    print("No of digits in factorial of",a,"is",len(z))
    
          
