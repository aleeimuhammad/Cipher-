alphabet=[chr(i) for i in range(97, 123)]*3
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
     shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text +=char
    return end_text
def brute_force_caesar(cipher_text):
    print("brute_forcing all possible shift amount...")
    for shift in range(78):
        decode_text = caesar(start_text=cipher_text, shift_amount=shift, cipher_direction="decode")
        print(f"shift amount {shift}:{decode_text}")
        
cipher_text = input ("enter the cipher text to brute force:\n").lower()
brute_force_caesar(cipher_text)                    
    
