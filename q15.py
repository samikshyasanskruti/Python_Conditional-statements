g=input("Enter gender(M/F):")
n1=input("Enter your name:")
n2=input("Enter your last name:")
a=int(input("Enter your age:"))
if(g=='F'):
   if(a>=10):
       s=input ("Are you married ?(Y/N):")
        if(s=='y'):
            print("I shall call you Mrs",n1,n2)
        else:
            print("I shall call you Ms",n1,n2)
elif (g=='M'):
         if(a>=20):
            print('I shall call you Mr',n1,n2)
        else:
             print('I shall call you ', n1,n2)
else(g=='F'):
n       if(a<=20):
             print('I shall call you ',n1,n2)

