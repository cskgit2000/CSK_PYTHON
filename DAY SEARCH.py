Day_Names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

Day_Num = int(input("Enter day number: "))
First_Day = input("First day of year: ")

if Day_Num < 2 or Day_Num > 365:
    print("Invalid Input")
else:
    Start_Day_Index = Day_Names.index(str.upper(First_Day))
    Current_Day_Index = Day_Num % 7 + Start_Day_Index - 1

    if Current_Day_Index >= 7:
       Current_Day_Index = Current_Day_Index - 7

    print("Day on day number", Day_Num, ":", Day_Names[Current_Day_Index])                   