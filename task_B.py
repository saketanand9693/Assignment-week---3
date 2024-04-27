while True:
    user_input = input("user input: ")
    
    if user_input.lower() == 'q':
        break
    
    words = user_input.split()
    output = ' ... '.join(words)
    
    print(output)
