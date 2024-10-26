a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=float(input("d: "))
e=float(input("e: "))
f=float(input("f: "))
check=(a*d)-(b*e)
if(check==0):
   print("No solution")
else:
   x=(e*d-b*f)/(a*d-b*c)
   y=(a*f-e*c)/(a*d-b*c)
   print('x:',x,'y:',y)
