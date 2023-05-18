a=int(input("Start"))
b=int(input("End"))
print("Prime numbers:")
for i in range(a,b+1):
    l=[]
    for j in range(1,i+1):
        if i%j==0:
            l.append(i)
    if len(l)==2:
        print(i)
        
    
