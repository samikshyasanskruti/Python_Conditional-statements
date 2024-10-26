w=float(input('enter weight(kg):'))
h=float(input('enter height(cm):'))
a=w/(h**2)
if(a<18.5):
   print('underweight')
elif(a>18.5 and a<24.9):
    print('normal weight')
elif(a>=25 and a <29.9):
    print("over weight")
else:
   print('obese')
