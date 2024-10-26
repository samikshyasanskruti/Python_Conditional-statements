n=int(input("scissors(0),rock(1),paper(2),enter your choice:"))
import random
c=random.randint(0,2)
if(n==0 and c==1):
    print("you lost")
elif(n==0 and c==2):
    print("you won")
elif(n==c):
    print("It is a draw")
elif(n==1 and c==2):
    print ("you lost")
elif(n==1 and c==0):
   print("you won")
elif(n==2 and c==0):
    print("you lost")
else:
    print("you won")     