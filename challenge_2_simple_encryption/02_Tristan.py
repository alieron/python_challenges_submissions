encoded_message = ""
decoded_message = ""

print('''
Please input your message in all lowercaps!!!
''')

def encrypt(dataToEncrypt):
    global encoded_message
    encryption = {
        "a": "b",
        "b": "c",
        "c": "d",
        "d": "e",
        "e": "f",
        "f": "g",
        "g": "h",
        "h": "i",
        "i": "j",
        "j": "k",
        "k": "l",
        "l": "m",
        "m": "n",
        "n": "o",
        "o": "p",
        "p": "q",
        "q": "r",
        "r": "s",
        "s": "t",
        "t": "u",
        "u": "v",
        "v": "w",
        "w": "x",
        "x": "y",
        "y": "z",
        "z": "a",
        " ": " "
    }

    encrypting = iter(dataToEncrypt)
    for x in encrypting:
        encryptedLetter = encryption.get(x)
        encoded_message += encryptedLetter
    print("encrypted message: " + encoded_message)

    def decrypt(dataToDecrypt):
        global decoded_message
        decryption = {
            "a": "z",
            "b": "a",
            "c": "b",
            "d": "c",
            "e": "d",
            "f": "e",
            "g": "f",
            "h": "g",
            "i": "h",
            "j": "i",
            "k": "j",
            "l": "k",
            "m": "l",
            "n": "m",
            "o": "n",
            "p": "o",
            "q": "p",
            "r": "q",
            "s": "r",
            "t": "s",
            "u": "t",
            "v": "u",
            "w": "v",
            "x": "w",
            "y": "x",
            "z": "y",
            " ": " "
        }

        decrypting = iter(dataToDecrypt)
        for x in decrypting:
            decryptedLetter = decryption.get(x)
            decoded_message += decryptedLetter
        print("decrypted message: " + decoded_message)

    decrypt(encoded_message)

userInput = input("Please input your message you want to encrypt: ")

encrypt(userInput)
