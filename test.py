# List of products with their prices
products = [
    ["Product 1", 10],
    ["Product 2", 20],
    ["Product 3", 30],
    ["Product 4", 40],
    ["Product 5", 50]
]

# Display available products
print("Available Products:")
for index, (name, price) in enumerate(products, 1):
    print(f"{index}. {name} - ${price}")

# Get user input
try:
    choice = int(input("\nEnter the product number to select: "))
    if 1 <= choice <= len(products):
        selected_product = products[choice-1]
        product_name = selected_product[0]
        product_price = selected_product[1]
        tax_rate = 0.15  # 15% tax
        tax_amount = product_price * tax_rate
        total_price = product_price + tax_amount
        
        print("\n" + "="*40)
        print(f"PRODUCT DETAILS".center(40))
        print("="*40)
        print(f"\nProduct: {product_name}")
        print("-"*40)
        print(f"Base Price:      ${product_price:9.2f}")
        print(f"Tax (15%):       ${tax_amount:9.2f}")
        print("-"*40)
        print(f"Total Price:     ${total_price:9.2f}")
        print("="*40)
    else:
        print("\n" + "!"*50)
        print("  INVALID SELECTION".center(50))
        print("!"*50)
        print(f"\nSorry, product number {choice} doesn't exist.")
        print(f"Please choose a number between 1 and {len(products)}.")
        print("\n" + "-"*50)
        # Show available products again
        print("\nAvailable Products:")
        for index, (name, price) in enumerate(products, 1):
            print(f"{index}. {name} - ${price}")
        print("\n" + "-"*50)
except ValueError:
    print("Please enter a valid number.")