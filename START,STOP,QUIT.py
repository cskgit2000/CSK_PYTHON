command=""
while command!="quit":
    command=input(">").lower()
    if command=="start":
        print("Car is started...")
    elif command=="stop":
        print("Car is stop")
else:
    print("ITS IS OVER!")