import sys
from Caesar import c_cipher
from Vigenere import v_cipher

if(len(sys.argv) != 4):
    print("Error:$'python3 Pypher.py [c/v] [encipher/decipher] ['Message'/'Cipher']'")
    exit()
    
code = sys.argv[1]
mode = sys.argv[2]
text = sys.argv[3]

if (code == "c"):
    c_cipher(mode, text)
    
elif (code == "v"):
    v_cipher(mode, text)

else :
    print("Error:$'python3 Pypher.py [c/v] [encipher/decipher] ['Message'/'Cipher']'")
    exit()
    
