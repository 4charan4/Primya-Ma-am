t=int(input("Enter temperature in deg C:"))
v=int(input("Enter windspeed in km/hr:"))
index=round(13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16)
print(index)
