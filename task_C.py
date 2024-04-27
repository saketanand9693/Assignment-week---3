def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels])

while True:
    user_input = input("Enter a string (q to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    result = remove_vowels(user_input)
    print("Vowels removed:", result)
