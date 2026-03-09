# Function to calculate the final price after applying a percentage discount
# This keeps the business logic separated from the input handling
def calculate_final_price(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


print("--- Professional Discount Calculator ---")

# Main program loop to allow multiple calculations without restarting the script
while True:
    try:
        # Taking input as a string first to allow the 'exit' command
        raw_price = input("Enter the original price (or 'exit' to quit): ")

        # Check if the user wants to terminate the program
        if raw_price.lower() == 'exit':
            print("Closing the program. Goodbye!")
            break

        # Convert inputs to float to handle decimal values (currency)
        price = float(raw_price)
        discount = float(input("Enter discount percentage (%): "))

        # Call the calculation function
        final_price = calculate_final_price(price, discount)

        # Display results formatted to 2 decimal places for currency standarts
        print(f"\nPrice Analysis:")
        print(f"Original Price: ${price:.2f}")
        print(f"Discount: {discount}%")
        print(f"Final Price: ${final_price:.2f}")
        print("-" * 30)

    except ValueError:
        # Handle cases where the user inputs text instead of numbers
        print("Error: Invalid input. Please enter a numerical value.")
