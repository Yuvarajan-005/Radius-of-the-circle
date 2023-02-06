#task1
from math import pi
r=float(input("Input the radius of the circle:"))
print("The radius of the circle is:"+str(pi*r**2))
#task2
fn=input("Inputthe fileName:")
f=fn.split(".")
if(f[-1]=='py'):
    print("The extension of the file is:'python'")

