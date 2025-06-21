n=int(input("ENTER NUMBER : "))
if n%2==0 :
    if 2<n<5:
        print("NOT WEIRD")
    elif 6<n<20:
        print('weird')
    elif n>20:
        print('not weird')
else:
    print("WEIRD")

