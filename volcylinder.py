r=float(input("Enter radius:"))
h=float(input("Enter height:"))
def vol(r,h):
    v=3.14*r*r*h
    return v
def sur(r,h):
    s=2*3.14*r*r+2*3.14*r*h
    return s
print(vol(r,h))
print(sur(r,h))
