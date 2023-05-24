a=int(input("Start table:"))
b=int(input("End table:"))
c=int(input("End:"))
for i in range(1,c+1):
    for j in range(a,b+1):
        print(j,"x",i,"=",i*j,end="\t")
    print(end="\n")

