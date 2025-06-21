#THIS IS KNOWN AS STRIP AND SPILIT FUNCTION
'''Cricket_player="Your favorite cricket player is : Msdhoni.His age is 43"
Cricketer_name=Cricket_player.split(":")[1].split(".")[0].strip()
print(Cricketer_name)'''
#MASKED MOBILE NUMBER
'''mobile='9765432101'
masked=mobile[:2]+'******'+mobile[-2:]
print(masked)'''
#POSITION FUNCTION
'''Cricket_player="Your favorite cricket player is : Msdhoni.His age is 43"
print("POSITION IS : ",Cricket_player.find('Msdhoni'))'''
#CONDITION+FOR LOOP IN ONE LINE
'''name='siva kumaran'
initials=([word[0].upper()for word in name.split()])
print(initials)'''
#WORD COUNT
'''Cricket_player="Your favorite cricket player is : Msdhoni.His age is 43"
word_count=len(Cricket_player.split())
print(word_count)'''
#title
'''Song='summertime saddness'
Customer='siva kumaran'
formatted=f'{Customer.title()} favorite song is {Song.title()}'
print(formatted)'''
#replace
'''location='chennai'
fixed_location=location.replace('chennai','kumbakonam')
print(fixed_location)'''