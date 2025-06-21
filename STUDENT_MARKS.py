n=int(input("ENTER NUMBER : "))
if n%2 and n>2 and n<5:
    print("NOT WEIRD")
elif n%2 and n>6 and n<20:
    print("WEIRD")
elif n%2 and n>20:
    print("NOT WEIRD")
else:
    print("WEIRD")
