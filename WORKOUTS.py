unit=input("IS THIS TEMPERATURE IS CELSIUS OR FARENHEIT(C/F) = ")
temp=float(input("ENTER THE TEMPERATURE = "))
if unit=="C":
    temp=round((temp*9)/5+32,1)
    print(f"THE TEMPERATURE IN FARENHEIT = {temp}°F")
elif unit=="f":
    temp=round((temp-32)*5/9,1)
    print(f"THE TEMPERATURE IN CELSIUS = {temp}°C")
else:
    print(f"Invalid Inputs")