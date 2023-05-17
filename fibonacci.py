a=0
b=1
n=int(input("Enter no. of terms:"))
print(a)
print(b)
def func():
    global c
    global a
    global b
    global n
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1
    if n>2:
        func()
func()
