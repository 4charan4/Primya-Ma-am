a=int(input("Enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))
if a<(b+c) and b<(a+c) and c<(a+b):
    print("Triangle is possible.")
else:
    print("Triangle is not possible.")
