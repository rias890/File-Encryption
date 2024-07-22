userinput = input("What is your text")
shift = int(input("What is your shift value?"))
encryptedText = ""
def caesar(userinput, shift):
    encryptedText = ""
    for c in userinput:
        alphabet = ord(c)+shift
        #print(alphabet)
        if alphabet> ord("z"):
            alphabet = alphabet-26
            #print(alphabet)
        if ord(c) == 32:
             alphabet = 32
             
        encryptedText+= chr(alphabet)
    print("Your text is: ",(encryptedText))

caesar(userinput, shift)




