a=int(input('Enter A = '))
b=int(input('Enter B = '))
Operation=input('add/sub/mul/div = ')
if (Operation=='add'):
    print(a+b)
elif(Operation=='sub'):
    print(a-b)
elif(Operation=='mul'):
    print(a*b)
elif(Operation=='div'):
    print(a//b)
else:
    print('Ivalid Operation')
