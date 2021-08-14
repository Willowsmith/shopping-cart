from typing import Dict
from collections import defaultdict

cart = defaultdict(int)

prices: Dict[str, float] = {
    "cherries": 1.25,
    "root beer": 2.36
}

def item_selection(action: str) -> str:
    return input(f"Which item do you want to {action}?")

def print_dict(d: defaultdict) -> None:
    for key, value in d.items():
        print(f"{key}: {value}")

def get_count(prompt: str) -> int:
    while True:
        try:
            n = int(input(prompt))
            if n < 1:
                print("Positive numbers only, try again.")
                continue
            return n
        except ValueError:
            print("Invalid input, try again.")
    
print(f"Available items: {', '.join(prices.keys())}")

while True:
    choice = input("Do you wish to 1: add an item to your cart, 2: delete an item from your cart, 3: view cart, or 4: checkout?")
    if choice == "1":
        item = item_selection("add to cart")
        if item not in prices:
            print(f"Item is not available, please choose again.")
            continue
        count = get_count("How many do you wish to add?")
        cart[item] += count
    elif choice =="2":
        item = item_selection("delete from cart")
        if item not in cart:
            print(f"This item does not exist in your cart.")
            continue
        count = get_count("How many do you wish to remove?")
        if count >= cart[item]:
            cart.pop(item)
            continue
        cart[item] -= count
        if cart[item] == 0:
            cart.pop(item)
    elif choice == "3":
        print_dict(cart)
        continue
    elif choice == "4":
        break
    else:
        print(f"{choice} is not a valid choice. You are just wrong, try again.")
total = 0
for item, count in cart.items():
    total += prices[item] * count
    
print(f"You owe me ${total}")
