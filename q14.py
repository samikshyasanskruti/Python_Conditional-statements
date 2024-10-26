n=int(input('enter a no:'))
if(n%5==0 and n%6==0):
      print('Is',n,'divisible by 5 and 6 ?True')
elif(n%5!=0 and n%6!=0):
     print('Is',n,'divisible by 5 and 6 ?False')
elif(n%5==0 and n%6!=0):
      print('Is',n,'divisible by 5 but not by 6 ?True')
else:
     print('Is',n,'divisible by 5 or 6 but not by both ?True')

