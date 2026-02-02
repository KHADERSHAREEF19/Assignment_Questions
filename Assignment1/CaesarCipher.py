def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    return result

def main():
    print("--- --- --- --- 🛠 Caesar Cipher Tool 🛠 --- --- ---  ---")
    choice = input("Enter 'E' to Encrypt & 'D' to Decrypt: ").upper()
    message = input("Message Please👉: ")
    
    try:
        shift_num = int(input("Shift number Please⏩: "))
    except ValueError:
        print("Invalid input. Please enter a whole number for the shift")
        return

    if choice == 'E':
        output = caesar_cipher(message, shift_num, mode='encrypt')
        print(f"\nEncrypted Message: {output}")
    elif choice == 'D':
        output = caesar_cipher(message, shift_num, mode='decrypt')
        print(f"\nDecrypted Message: {output}")
    else:
        print("Error❌ Please select 'E' or 'D'")

if __name__ == "__main__":
    main()