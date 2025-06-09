def main():
    # Initialize counters for positive numbers, negative numbers, and zeros
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Start a loop to repeatedly ask the user for input
    while True:
        user_input = input("Enter a number (or q to quit): ")
        
        # If the user types 'q' (case insensitive), break the loop to quit
        if user_input.lower() == 'q':
            break
        
        try:
            # Try converting the input to a float
            number = float(user_input)
            
            # Increment the appropriate counter based on the value
            if number > 0:
                positive_count += 1
            elif number < 0:
                negative_count += 1
            else:
                zero_count += 1
        except ValueError:
            # If the input is not a valid number, show an error message
            print(f"{user_input} is not a number. Enter a number (or q to quit):")

    # Display the final counts after the user quits
    print(f"\nYou entered {positive_count} positive number(s), "
          f"{negative_count} negative number(s) and {zero_count} zero(s).")

# This ensures the program runs when executed directly
if __name__ == "__main__":
    main()