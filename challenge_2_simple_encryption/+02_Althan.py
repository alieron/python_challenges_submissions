import random
random.seed()
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
crypt = []
task = input("Encrypt or Decrypt? ")
def findseed(): #Determining the seed. When encrypting, a new seed is generated, while when decrypting, seed is inputted by the user.
    if task == "Encrypt":
        return(random.randint(0,100))
    elif task == "Decrypt":
        return(int(input("What was your encryption key? " )))
    else:
        print("Please say 'Encrypt' or 'Decrypt'. (Caps sensitive) ")
        exit()
seed = findseed()
random.seed(seed)
x = 0
for x in range(52): #Arranging the list in an order unique to the seed. Crypt is the new list ordered in the random order unique to the seed
    x = alphlist[random.randint(0,len(alphlist)-1)]
    alphlist.remove(x)
    crypt.append(x)
output = ""
message = input("What is the message to encrypt/decrypt? ")
if task == "Encrypt":
    for i in message:
        if i in alphabets:
            output += crypt[alphabets.index(i)] #if the character is an alphabet, add encrypted character into the ouput
        else:
            output += i #if the character is not an alphabet, do not encrypt character
if task == "Decrypt":
    for i in message:
        if i in alphabets:
            output += alphabets[crypt.index(i)]
        else:
            output += i
print("Your encryption key is " + str(seed))
print("Your output message is '" + output + "'")