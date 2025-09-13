'''
create a shopping cart that continuasly asks for a food pproduct and price from the user
have an exit option if a user wants to stop adding things to their card
show a list of items and the total of the items in the cart 

'''

food_items = []
item_prices = []
total = 0

#Item_dictionary = {food_item: item_price}

while True:
    food = input("Enter an item to cart  or Q to quit: ")
    
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price : R"))
    food_items.append(food)
    item_prices.append(price)


print('***********YOUR CART***********')

for  food in food_items:   
    print(food, '\n')
    #print(item_prices, '\n')

for price in item_prices:
    total += price

print("You total is R{total}", '\n')