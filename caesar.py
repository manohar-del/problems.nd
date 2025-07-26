def caesarEncrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            c = (p + shift) % 26
            result += chr(base + c)
        else:
            result += char
    return result

def caesarDecrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            c = ord(char) - base
            p = (c - shift) % 26
            result += chr(base + p)
        else:
            result += char
    return result

text = input("Enter the message: ")
shiftValue = int(input("Enter the shift value: "))
mode = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()

if mode == 'encode':
    print("Encoded message:", caesarEncrypt(text, shiftValue))
elif mode == 'decode':
    print("Decoded message:", caesarDecrypt(text, shiftValue))
else:
    print("Invalid mode selected.")