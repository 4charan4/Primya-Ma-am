n=int(input("Enter number of numbers:"))
a=[]
for i in range(0,n):
    b=int(input("Enter number:"))
    a.append(b)
x=int(input("Enter element to be found:"))
pos=[]
neg=[]
t=0
for i in range(0,n):
    if x==a[i]:
        t=1
        pos.append(i)
        neg.append(-len(a)+i)

neg1=neg[::-1]

if t==0:
    print("Element is not found.")
else:
    print("Element is found",len(pos),"times")
    print("Positive index:",pos)
    print("Negative index:",neg1)



