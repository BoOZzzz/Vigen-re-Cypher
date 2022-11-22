#!/usr/bin/env python
#generate key
def generateKey(text,keyWord):
    key = ""
    for i in range (0, len(text)):
        x = i;
        if x >= len(keyWord):
            x = x%len(keyWord)
        key += keyWord[x]
    return key


#encrypt with key
def encryptText(text, key):
    caps = text.upper()
    encryptedText = ""
    keyIndex = 0
    for i in range(len(text)):
        uni = ord(caps[i])
        x = 0
        if(uni < 65 or (uni > 90 and uni < 97) or uni >122):
            encryptedText += text[i]
        else:
            x = (ord(caps[i])+ord(key[keyIndex]))%26 + 65
            if (text[i].islower()):
                encryptedText += chr(x+32)
                keyIndex += 1
            else:
                encryptedText += chr(x)
                keyIndex +=1
    return (encryptedText)

if __name__ == "__main__":
    text = input("enter text: ")
    keyWord = input("enter key word: ")
    key = generateKey(text,keyWord)
    print(encryptText(text, key))
