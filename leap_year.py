a=int(input("Enter a year:"))
'''if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a,"is a leap year.")#divisible by 400
        else:
            print(a,"is not a leap year.")#divisible by 100 not 400
    else:
        print(a,"is a leap year.")#divisible by 4 not 100
else:
    print(a,"is not a leap year.")#not divisible by 4'''



if(a%4==0 and a%100!=0) or a%400==0:
    print(a,"is a leap year.")
else:
    print(a,"is not a leap year.")

    


# a%100==0 must be given with or...or else divisible of 100 will be considered leap years
    
        
    
