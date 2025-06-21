#NESTED if CONDITION
age=18
has_licensed='No'
if age>=18:
    if has_licensed=='Yes':
        print('YOU CAN DRIVE')
    else:
        print('GO AND TAKE LICENSE')
else:
    print('YOU ARE TOO YOUNG')