secreat_sn="StrangerThings"
count=1
limit=3
while count<limit:
    g_sn=input("Enter Series Name=")
    count +=1
    if g_sn==secreat_sn:
        print("It is correct!")
        break
else:
    print("OOPS!")