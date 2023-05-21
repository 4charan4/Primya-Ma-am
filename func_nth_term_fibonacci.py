n=int(input("Enter n:"))
a=0
b=1
def func():
    global a
    global b
    global c
    global n
    c=a+b
    a=b
    b=c
    n=n-1
    if n>2:
        func()
    else:
        print(c)
func()
        
