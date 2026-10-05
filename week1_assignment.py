# Ask the user for the price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

# Calculate the total
total = price * quantity

# Print a friendly summary with an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
