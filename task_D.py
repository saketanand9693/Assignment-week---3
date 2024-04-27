while True:
    user_input = input("Enter a number (q to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    try:
        number = int(user_input)
        bytes_needed = (number.bit_length() + 7) // 8
        print(f"Number {number} requires {bytes_needed} bytes for its binary representation.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
