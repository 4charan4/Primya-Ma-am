dict1 = {}
n=int(input("Enter number of elemnts:"))
for i in range(n):
    key = input("Enter employee's name: ")
    val = input("Enter employee's salary: ")
    dict1[key] = val
print(dict1)


for key in dict1:
    print(key,dict1[key])

