import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result

def encrypt_text():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    messagebox.showinfo("Encrypted Text", f"Original Text: {text}\nShift: {shift}\nEncrypted Text: {encrypted_text}")

def decrypt_text():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher(text, -shift)
    messagebox.showinfo("Decrypted Text", f"Original Text: {text}\nShift: {shift}\nDecrypted Text: {decrypted_text}")

def encrypt_and_decrypt_text():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    decrypted_text = caesar_cipher(encrypted_text, -shift)
    messagebox.showinfo("Encrypt & Decrypt", f"Original Text: {text}\nShift: {shift}\nEncrypted Text: {encrypted_text}\nDecrypted Text: {decrypted_text}")

root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Enter a sentence:").grid(row=0, column=0, padx=10, pady=10)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter shift value:").grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

encrypt_decrypt_button = tk.Button(root, text="Encrypt & Decrypt", command=encrypt_and_decrypt_text)
encrypt_decrypt_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()