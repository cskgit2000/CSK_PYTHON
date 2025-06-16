acc=[]
def ca(ano):
    name=input("ENTER NAME : ")
    amt=int(input("ENTER  AMOUNT : "))
    acc.append([name,ano,amt])
    print(acc)
def dep():
    ano=int(input("ENTER ACCOUNT NUMBER : "))
    amt=int(input("ENTER AMOUNT : "))
    for ac in acc:
        if ac[1]==ano:
            ac[2]+=amt
            break
    print(acc)
def wd():
    ano=int(input("ENTER ACCOUNT NUMBER : "))
    amt=int(input("ENTER AMOUNT : "))
    for ac in acc:
        if ac[1]==ano:
            if ac[2]-amt>=0:
                ac[2]-=amt
                print(ac)
            else:
                print("INSUFFICENT BALANCE")
            break
def be():
    ano=int(input("ENTER ACCOUNT NUMBER : "))
    for ac in acc:
        if ac[1]==ano:
            print(ac[2])
ano=100
while True:
    print("1.CREATE ACCOUNT  \n2.DEPOSIT  \n3.WITHDRAWAL  \n4.BALANCE ENQUIRY  \n5.EXIT  ")
    ch=int(input("ENTER YOUR CHOICE : "))
    if ch==1:
        ano+=1
        ca(ano)
    elif ch==2:
        dep()
    elif ch==3:
        wd()
    elif ch==4:
        be()
    else:
        break