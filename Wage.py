a=int(input("Enter your age:"))
if a<18 or a>40:
    print("Invalid age.")
    break
b=input("Enter M if male and F if female:")
if a!=('M' or "F"):
    print("Invalid gender.")
    break
c=int(input("No.of days at work:"))
if a>=18 and a<30:
    if b=='M':
        print("Your total wage is:",700*c)
    else:
        print("Your total wage is:",750*c)
else:
    if b=='M' or b=='F':
        print("Your total wage is:",800*c)








        
