a=int(input("Enter food rating from 1 to 5:"))
b=int(input("Enter service rating from 1 to 5:"))
c=int(input("Enter ambience rating from 1 to 5:"))
d=int(input("Enter bill amount:"))
if a==4 or a==5:
    if (b==4 or b==5) and (c==4 or c==5):
        tip=(10/100)*d
    else:
        tip=(5/100)*d
else:
    if (b==4 or b==5) and (c==4 or c==5):
        tip=(5/100)*d
    else:
        tip=(1/100)*d
print("Tip amounts to Rs.",tip)



