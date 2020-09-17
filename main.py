# Vigenere cipher in python
import platform    # For getting the operating system name


def inputs():
    global text
    global key
    global mode

    try:
        text = str(input("Enter a message to encrypt or decrypt: "))
        key = str(input("Enter a key for encryption or decryption: "))
        mode = int(input("Choose a mode; 0 for encryption, and 1 for decryption: "))
    except ValueError:
        print("Dumb shit happened")
        pass


def cipher(ctext, ckey, cmode):

    # Initialize vars and chars
    # ============================================ #
    msgchar = ''
    textint = [ord(i) for i in ctext]
    cipherint = [ord(i) for i in ctext]
    keyint = [ord(i) for i in ckey]
    keylen = len(ckey)

    # ============================================ #

    # Encrypt
    # ============================================ #
    if cmode == 0:
        for i in range(len(textint)):
            adder = keyint[i % keylen]
            adder *= -1

            # Converty the array of integer ascii characters to a string
            v = (textint[i] - 32 + adder) % 95
            msgchar += chr(v + 32)

        print(msgchar)
        return msgchar
    # ============================================ #

    # Decrypt
    # ============================================ #
    elif cmode == 1:
        for i in range(len(cipherint)):
            adder = keyint[i % keylen]
            adder *= +1

            # Converty the array of integer ascii characters to a string
            v = (cipherint[i] - 32 + adder) % 95
            msgchar += chr(v + 32)

        print(msgchar)
        return msgchar
    # ============================================ #


def clr():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    return subprocess.call(command) == 0

# Infinate program loop
while True:
    # why does it say error it works
    inputs()
    cipher(text, key, mode)
