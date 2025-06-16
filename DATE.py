months = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"]

dateStr = input("Enter date in MMDDYYYY format: ")
monthIndex = int(dateStr[:2]) - 1
month = months[monthIndex]
day = dateStr[2:4]
year = dateStr[4:]

newDateStr = month + ' ' + day + ', ' + year
print(newDateStr)