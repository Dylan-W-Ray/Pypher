#English alphabet to be used in
#decipher/encipher calculations.
Alpha=['a','b','c','d','e','f','g',
       'h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u',
       'v','w','x','y','z']

def c_cipher(mode, text):

    if(mode == "decipher"):
    
        #The encoded cipher is given as a
        #commandline argument.
        cipher = text
        
        #Determining the number of english
        #letters in the cipher.
        cipherLettCount = 0;
        for c in cipher:
            if((ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)):
                cipherLettCount += 1
                
                
        #Making the cipher frequency array
        cipherLow = cipher.lower()
        cipherFreq = [0.00]*26
        for l in range(26):
            charCount = 0
            for c in range(len(cipherLow)):
                if(Alpha[l] == cipherLow[c]):
                    charCount += 1
                    cipherFreq[l] = float(charCount) / float(cipherLettCount)
                            
                            
        print("Cipher Frequency:")            
        print(cipherFreq)
                    
        #Value of the frequency for a givne letter
        #in the 
        def f(c):
            return cipherFreq[c]
                            
        #Function to return a certian index's,
        #representing a certian letter's, 1-gram
        #english plain text frequency.
        def p(x):

            plainTxtFreq = [0.080,0.015,0.030,0.040,
                            0.130,0.020,0.015,0.060,
                            0.065,0.005,0.005,0.035,
                            0.030,0.070,0.080,0.020,
                            0.002,0.065,0.060,0.090,
                            0.030,0.010,0.015,0.005,
                            0.020,0.002]
            return plainTxtFreq[x]
        
        #Making the 1-gram correlation frequency
        #between the cipher text and the english
        #language, per one character at a time.
        def phi(i):
            correlFreq = 0.0
            
            for c in range(26):
                correlFreq += f(c)*p(c-i)
                
            return correlFreq
                                
                                
        #Decoding the cipher one letter at a time
        def D(k):
            plainTxt = ""
            
            for i in range(len(cipher)):
                if(ord(cipher[i]) >= 65 and ord(cipher[i]) <= 90):
                    cNum = ord(cipher[i]) - 65
                    dec = (26 + cNum - k) % 26
                    plainTxt += chr(dec + 65)
                    
                elif(ord(cipher[i]) >= 97 and ord(cipher[i]) <= 122):
                    cNum = ord(cipher[i]) - 97
                    dec = (26 + cNum - k) % 26
                    plainTxt += chr(dec + 97)
                    
                else:
                    plainTxt += cipher[i]
                    
            print(plainTxt)    
                    
                                            
                                            
        #main part of the program for decoding starts here.
        print("Correlation Frequency:")
        for i in range(26):
            print("key-", i, ":", round(phi(i), 4))
        
        answer = "y"

        while(answer == "y" or "Y" or  "Yes" or "YES"):    
            answer = input("Would you like to try a key (y/n):")
        
            if(answer != "y" or not "Y" or not "Yes" or not "YES"):
                exit()
            else:
                key = input("Key:")
                print("decrytping with key " + key + ":")
                D(int(key))
                                                        
                                                        
                                                        
                                                        
    #Encoding part of the program starts here.                
    if(mode == "encipher"):
        plainTxt = text
        
        key = input("Please choose a key(0->25):")
        key = int(key)
        
        cipher = ""
        
        for i in range(len(plainTxt)):
            if(ord(plainTxt[i]) >= 65 and ord(plainTxt[i]) <= 90):
                m = ord(plainTxt[i]) - 65
                ciphChar = ((m + key) % 26)
                cipher += Alpha[ciphChar].upper()
                
            elif(ord(plainTxt[i]) >= 97 and ord(plainTxt[i]) <= 122):
                m = ord(plainTxt[i]) - 97
                ciphChar = ((m + key) % 26)
                cipher += Alpha[ciphChar]
            else:
                cipher += plainTxt[i]
                
        print("Cipher:", cipher)
