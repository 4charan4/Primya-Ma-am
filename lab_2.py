a=input("Enter a string:")
b=input("Enter a string:")
c=list(a)
d=list(b)
for i in c:
    if i in d:
        d.remove(i)
if len(d)==0:
    print("yes")
else:
    print("no")
    
