foods = []
prices = []
total = 0

while True:
    food=input("ENTER THE FOOD TO BUY = ")
    if food=="q":
        break
    else:
        price=float(input(f"ENTER THE PRICE OF {food} = $"))
        foods.append(food)
        prices.append(prices)

print("----CART----")

for food in foods:
    print(food,end=" ")
    