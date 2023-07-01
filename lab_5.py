a=set(input("Enter a set:"))
b=set(input("Enter another set:"))
print(a)
print(b)
if len(a)>=len(b):
    print(b.issubset(a))
else:
    print(a.issubset(b))
