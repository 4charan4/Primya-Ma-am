import math
def check_square(a):
    b=int(math.sqrt(a))
    if b*b==a:
        print("Perfect Square")
    else:
        print("Not a perfect square")
a=int(input("Enter a number."))
check_square(a)
    
    
