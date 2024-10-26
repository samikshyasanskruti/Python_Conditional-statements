rahul=int(input('enter rahul age:'))
ayush=int(input('enter ayush age:'))
ajay=int(input('enter ajay age:'))
if(rahul>ayush and rahul>ajay):
  print('rahul is elder among all')
elif(ayush>rahul and ayush>ajay):
  print('ayush is elder among all')
elif(ajay>rahul and ajay>ayush):
  print('ajay is elder among all')
else:
  print("there is ba tie between their age")
