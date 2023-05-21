print("SIMPLE INTEREST CALCULATION:")
def interest_calculation(P,N,R):
    return P*N*R/100
name=input("Enter your name:")
age=int(input("Enter your age:"))
gender=input("Enter 'M' if male and 'F' if female:")
P=int(input("Enter your Principal amount:"))
N=int(input("Enter the number of years:"))
if age>=60:
    if gender=='M' or gender=='F':
        R=12
else:
    if gender=='M':
        R=9
    elif gender=='F':
        R=10
    else:
        print("Gender invalid")
    #break
print(name,", your interest:",interest_calculation(P,N,R))

    

    
    
