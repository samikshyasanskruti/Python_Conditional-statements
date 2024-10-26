x=float(input('enter the x coordinate:'))
y=float(input('enter the y coordinate:'))
if (x==0 and y==0):
    print ('the point is at origin')
elif(x==0 and y!=0):
   print("the point is on y axis")
elif(x!=0 and y==0):
    print("the point is on x axis")
elif(x>0 and y>0):
   print("the point lies on 1st quadrant")
elif(x<0 and y>0):
   print("the point lies on 2nd quadrant")
elif(x<0 and y<0):
    print("the point lies on 3rd quadrant")
else:
    print("the point lies on 4th quadrant")
    