#Write a python script that traverses through an input string 
#and prints its characters in different lines - two characters per line.
name=input("ENTER NAME : ")
for i in range(0,len(name),2):
    print(name[i:i+2])