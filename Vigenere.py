#English alphabet to be used in
#decipher/encipher calculations.
Alpha=['a','b','c','d','e','f','g',
       'h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u',
       'v','w','x','y','z']

def v_cipher(mode, text):
    
    if(mode == "encipher"):
        
        plainTxt = text
        cipher = ""
        
        key = input("Key:")
        key = key.upper()
        
        if(len(key) > len(plainTxt.strip())):
            print("Error key is larger than the message")
            exit()
            
        keyIndex = 0
        for c in plainTxt:
                
            if(ord(c) >= 65 and ord(c) <= 90):
                m = ord(key[keyIndex]) - 65
                k = ord(c) - 65
                cipherCharNum = (m + k) % 26
                cipherChar = Alpha[cipherCharNum].upper()
                cipher += cipherChar
                
                keyIndex += 1
                keyIndex %= len(key)
                
            elif(ord(c) >= 97 and ord(c) <= 122):
                m = ord(key[keyIndex]) - 65
                k = ord(c) - 97
                cipherCharNum = (m + k) % 26
                cipherChar = Alpha[cipherCharNum]
                cipher += cipherChar
                
                keyIndex += 1
                keyIndex %= len(key)
                
            else:
                cipher += c
                
        print("Cipher:", cipher)
                    
                    
    elif(mode == "decipher"):
        
        cipher = text 
        
        plainTxt = ""
        
        key = input("Key:")
        key = key.upper()
        
        if(len(key) > len(cipher.strip())):
            print("Error key is larger than the cipher")
            exit()
            
        keyIndex = 0
        for c in cipher:
            
            if(ord(c) >= 65 and ord(c) <= 90):
                k = ord(key[keyIndex]) - 65
                cNum = ord(c) - 65
                plainCharNum =(26 + cNum - k) % 26
                plainTxtChar = Alpha[plainCharNum].upper()
                plainTxt += plainTxtChar
                
                keyIndex += 1
                keyIndex %= len(key)
                
            elif(ord(c) >= 97 and ord(c) <= 122):
                k=ord(key[keyIndex]) - 65
                cNum=ord(c) - 97
                plainCharNum = (26 + cNum - k ) %26
                plainTxtChar=Alpha[plainCharNum]
                plainTxt += plainTxtChar
                
                keyIndex += 1
                keyIndex %= len(key)
                
            else:
                plainTxt += c
                
        print("Message:", plainTxt)
