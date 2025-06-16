#count
'''count=5
while count>0:
    print(f'Count down from :{count}')
    count-=1
print('Times UP')'''
#append
items=[]
while True:
    item=input("Product Name(type 'done' to finish) : ")
    if item.lower()=='done':
        break
    items.append(item)
print(items)