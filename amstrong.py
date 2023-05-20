print("Amstrong numbers:")
for i in range(100,1001):
    temp=i
    sum=0
    while i!=0:
        a=i%10
        sum=sum+a**3
        i=i//10
    if sum==temp:
        print(temp)
        

    
