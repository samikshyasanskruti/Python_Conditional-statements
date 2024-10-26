n=int(input("enter today day:"))
d=int(input('enter number of days elapsed till today:'))
j=n+(d//7)
if(j==1):
      print("Monday")
elif(j==2):
    print("Tuesday")
elif(j==3):
    print("Wednesday")
elif(j==4):
    print("Thursday")
elif(j==5):
    print("Friday")
elif(j==6):
     print("Saturday")
else:
    print("Sunday")
