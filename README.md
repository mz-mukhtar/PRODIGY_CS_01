# Caesar Cipher (Interactive Encryption & Decryption)

---

## Disclaimer

This project is strictly for **educational purposes only**.  
The Caesar Cipher is a very simple, ancient encryption method and **should not be used for real security** in any serious application.  
Do not use this to hide sensitive information — it’s trivial to break.  
Use responsibly, for learning and practice only.

---

## Theoretical Overview

The **Caesar Cipher** is one of the oldest and simplest forms of encryption.  
It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

~~~
Plain: HELLO
Cipher: KHOOR
~~~


Decryption reverses the shift using the same key:

~~~
Cipher: KHOOR
Plain: HELLO
~~~


This cipher only changes letters; numbers and punctuation stay the same.

---

## How It Works

### This Python program lets you:
- Choose whether to **encrypt** or **decrypt** a message.
- Enter a shift key (an integer).
- It then performs the operation and prints the result.

### The program handles:
- Both uppercase and lowercase letters.
- Non-alphabet characters (kept unchanged).
- Negative shifts (shift left) and large shifts (it wraps correctly).

---

## How to Use

### Requirements

- Python 3.x installed on your computer.
- No external libraries needed.

---

### Download the Project

~~~
# Clone this repository
git clone https://github.com/mz-mukhtar/PRODIGY_CS_01.git

# Navigate into the project folder
cd PRODIGY_CS_01
~~~

### Run the Program
~~~
# Run the script using Python
python caesar_cipher.py
~~~
