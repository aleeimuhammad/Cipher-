alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_brute_force(start_text, cipher_direction):
    for shift_amount in range(26):
        end_text = ""
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                if cipher_direction == "decode":
                    shift_amount = -shift_amount
                new_position = (position + shift_amount) % 26
                end_text += alphabet[new_position]
                if cipher_direction == "decode":
                    shift_amount = -shift_amount
            else:
                end_text += char
        print(f"Shift {shift_amount}: {end_text}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid option. Please choose 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    
    caesar_brute_force(start_text=text, cipher_direction=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye!")
