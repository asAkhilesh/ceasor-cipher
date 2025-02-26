# Caesar Cipher GUI with Python & Tkinter 🔐

This project is a simple **Caesar Cipher** encryption and decryption tool built using **Python** and **Tkinter**. It allows users to input a sentence, select a shift value, and encrypt or decrypt the text with a single click.

## Features ✨
- **Encrypt a sentence** using the Caesar Cipher algorithm.
- **Decrypt a sentence** back to its original form.
- **Encrypt & Decrypt in one step** to verify results.
- Simple and user-friendly **GUI** built with Tkinter.

## How It Works ⚙️
1. Enter the text you want to encrypt or decrypt.
2. Provide a shift value (an integer for letter shifting).
3. Click the respective button:
   - **Encrypt**: Encrypts the input text.
   - **Decrypt**: Decrypts the input text.
   - **Encrypt & Decrypt**: Encrypts and then immediately decrypts the text to verify results.
4. View the results in a pop-up message box.

## Installation & Usage 🛠️
### Prerequisites:
- Python 3.x installed on your system.

### Steps to Run the Program:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/caesar-cipher-gui.git
   cd caesar-cipher-gui
   ```
2. Run the script:
   ```bash
   python caesar_cipher.py
   ```

## Code Explanation 📜
The project consists of:
- **Caesar Cipher Function**: Shifts each letter of the input text forward or backward based on the shift value.
- **Encrypt & Decrypt Functions**: Calls the cipher function to perform encryption and decryption.
- **Tkinter GUI**: Provides a user interface to input text, specify the shift value, and trigger encryption/decryption.

## Example 📌
**Input:**
```
Hello, World!
Shift: 3
```
**Encrypted Output:**
```
Khoor, Zruog!
```
**Decrypted Output:**
```
Hello, World!
```

## Contributing 🤝
Feel free to fork this repository and improve the project! You can:
- Add more encryption algorithms.
- Enhance the GUI with more styling.
- Improve error handling for invalid inputs.

## License 📜
This project is open-source and available under the **MIT License**.

---
**Happy Coding! 🚀**

