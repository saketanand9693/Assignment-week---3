# Python Program for Altering Case of User Input

while True:
    # Prompt user for input
    user_input = input("Enter a string (or 'q' to quit): ")

    # Check if user wants to quit
    if user_input.lower() == 'q':
        print("Exiting the program...")
        break

    # Alter the case of the input
    altered_input = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(user_input))

    # Display the altered input
    print("Altered Case:", altered_input)
