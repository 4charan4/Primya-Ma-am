a=int(input("Start:"))
b=int(input("End:"))
ecount=0
ocount=0
for i in range(a,b+1):
    if i%2==0:
        ecount=ecount+1
    else:
        ocount=ocount+1
print("Odd:",ocount)
print("Even:",ecount)
