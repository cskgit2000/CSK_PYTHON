Weight=int(input("ENTER WEIGHT ="))
Unit=input("(L)bs or (K)g =")
if Unit.upper()=="L":
    Converted=Weight*0.45
    print(f"You are{Converted}into kilos")
else:
    Converted=Weight/0.45
    print(f"You are {Converted} into pounds")