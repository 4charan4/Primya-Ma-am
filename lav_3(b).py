n=int(input("Enter number of numbers:"))
l=[]
for i in range(0,n):
    a=int(input("Enter number:"))
    l.append(a)
print("Original list:",l)

if len(l)==1:
    t=0
else:
    for i in range(0,n-1):
        if l[i]<=l[i+1]:
            t=0
        else:
            t=1
            break

if t==0:
    print("Yes,List is in ascending order")
else:
    print("No,List is not in ascending order")

