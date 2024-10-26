c=input('enter a character:')
ascii_value=ord(c)
if(65<=ascii_value<=90):
    print(c," is a capital letter")
elif(97<=ascii_value<=122):
    print(c,"is a small letter")
elif(48<=ascii_value<=57):
    print(c," is a digit")
elif(0<=ascii_value<=47)or(58<=ascii_value<=64) or(91<=ascii_value<=96) or(123<=ascii_value<=127):
    print(c,"is a special character")
else:
    print('invalid character')
