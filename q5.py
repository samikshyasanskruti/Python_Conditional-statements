a=float(input('enter value of a:'))
b=float(input('enter value of b:'))
c=float(input('enter value of c:'))
d=b**2-(4*a*c)
import math
r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)
if(d==0):
 print('one root:',r1)
elif(d>0):
    print('two roots',r1,', ',r2)
else:
    print('No real roots')
