m=int(input('enter the month'))
y=int(input('enter the year'))
assert(m>=1) or(m<=12),"invalid month"
assert (y>=1582),"no record found"
if((y%100==0 or y%4==0) and m==2):
 m=29
elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    m=31
else:
   m=30
   if(m==1):
      d='jan'
   elif(m==2):
      d='feb'
   elif(m==3):
      d='mar'
   elif(m==4):
      d='apr'
   elif(m==5):
       d='may'
   elif(m==6):
       d='jun'
   elif(m==7):
       d='jul'
   elif(m==8):
        d='aug'
   elif(m==9):
        d='sep'
   elif(m==10):
        d='oct'
   elif(m==11):
       d='nov'
   elif(m==12):
       d='dec'
   else:
       d='invalid'
print(d,y,'had',m,'days')
        
        