price = float(input("Enter a price: "))
print(f"Price: R${price:<10.2f}!")
print(f"Price: R${price:>10.2f}!")
print(f"Price: R${price:^10.2f}!")
print(f"Price: R${price:_^10.2f}!")  # Put characters between empty spaces
print(f"Full price: R${int(price):_^10}!") # Functions inside the f-string
print(f"Price: R${int(price * 10):>10.2f}!") # Perform mathematical operations
print(f"""The price is R${price:_^10.2f}.\nAnd you can buy lots of sweets!""")