a=int(input("Start table:"))
b=int(input("End table:"))
c=int(input("End:"))
for i in range(a,b+1):
    for j in range(1,c+1):
        print(i,"x",j,"=",i*j)
        

