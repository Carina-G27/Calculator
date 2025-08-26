def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    return price
price = float(input("Enter the original price: ")) # Get user input
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent) # Calculate and display the final price
print(f"The final price is: ${final_price:.2f}")