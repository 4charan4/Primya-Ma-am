import math
def sphere(r,x=math.pi):
    v=4/3*x*r**3
    sa=4*x*r**2
    return v,sa
def cylinder(r,h,x=math.pi):
    v=x*r**2*h
    sa=2*x*r*h+2*x*r**2
    return v,s
def cone(r,h,s,x=math.pi):
    v=1/3*x*r**2*h
    sa=x*r*s+x*r*h
    return v,s
def rect_prism(l,w,h):
    v=lwh
    sa=2(l*b+b*h+l*h)
    return v,s
def tri_prism(l,b,h,s):
    v=1/2*b*l*h
    sa=b*h+l*b+2*l*s
    return v,s
a=int(input("Choose 1 for sphere, 2 for cylinder, 3 for cone, 4 for rectangular prism and 5 for triangular prism:"))
if a==1:
    r=int(input("Enter radius:"))
    print("Area and volume:",sphere(r))
elif a==2:
    r=int(input("Enter radius:"))
    h=int(input("Enter height:"))
    print("Area and volume:",cylinder(r,h))
elif a==3:
    r=int(input("Enter radius:"))
    h=int(input("Enter height:"))
    s=int(input("Enter slant height:"))
    print("Area and volume:",cone(r,h,s))
elif a==4:
    l=int(input("Enter length:"))
    h=int(input("Enter height:"))
    w=int(input("Enter width:"))
    print("Area and volume:",rect_prism(l,h,w))
elif a==5:
    l=int(input("Enter length:"))
    h=int(input("Enter height:"))
    s=int(input("Enter side of triangle:"))
    b=int(input("Enter base of triangle:"))
    print("Area and volume:",tri_prism(l,b,h,s))
else:
    print("Invalid!")

    


    
