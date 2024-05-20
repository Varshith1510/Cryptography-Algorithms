import numpy as np
import string

letters = list(string.ascii_lowercase) 


def display_vigenere(table):
    ''' This function displays the vigenere table'''
    for row in table:
        for num in row:
            print(num,'',end = '')
        print()
        
        
def encryption(plain,key):
    ''' This function performs the conversion of plain text into cipher text'''
    cipher_text = ''
    
    # For each iteration, look at the intersection of plain text char row & key column
    plain_chars = list(plain)
    key_chars = list(key)
    
    combined = zip(plain_chars,key_chars)
    
    for pair in combined: # Pair contains corresponding plain text char & key char
        cipher_char = vigenre_table[chars[pair[0]]][chars[pair[1]]]        
        cipher_text += cipher_char
        
    return cipher_text


def decryption(cipher,key):
    ''' This function performs the conversion of cipher text into plain text '''
    plain_text = ''
    
    # For each iteration, look at the key char row & find the cipher char in that row
    # Corresponding column index is the plain text char
    
    cipher_chars = list(cipher)
    key_chars = list(key)
    
    combined = zip(key_chars,cipher_chars)
    
    for pair in combined:
        row = vigenre_table[chars[pair[0]]] # Find the key char row
        pos = row.index(pair[1]) # Find the position of the cipher char in that row
        plain_char = letters[pos] # Corresponding column index is the plain text char
        plain_text += plain_char
        
    return plain_text
        

chars = {}

# Creating a char-num mapping
for i in range(len(letters)):
    chars[letters[i]] = i  
    
    
vigenre_table = []

# Create a 26 * 26 matrix -> Vigenere's Table
for i in range(len(letters)):
    row = [] # Each row contains the set of 26 alphabets in different order
    for j in range(len(letters)):
        row.append(letters[(i+j)%26]) # During each iteration, each row should start with a different alphabet
    vigenre_table.append(row)
    

print("Welcome to Vigenere's Cipher!\nWhat operation would you like to perform?\n\n1. Encryption\n2. Decryption")
choice = int(input("Enter your choice: "))

if (choice == 1): # i.e. Encryption
    plain_text = input("Enter a string: ").lower()
    key = input("Enter the key: ").lower()
    
    if (len(key) < len(plain_text)):
        # Both key & plain text should be of same length
        diff = len(plain_text) - len(key)
        key = key * diff # Creating multiple copies of the key
        key = key[:len(plain_text)] # Creating key same as length of plain text
        
        print("Encrypted text: ",encryption(plain_text, key))
        
    elif(len(key) > len(plain_text)):
        print("Enter a key which is of same length as the plain text!")
    
    
if (choice == 2): # i.e. Decryption
    cipher_text = input("Enter a string: ").lower()
    key = input("Enter the key: ").lower()
    
    # Cipher text & key length should be the same
    if(len(key) < len(cipher_text)): 
        diff = len(cipher_text) - len(key)
        key = key * diff # Creating copies of the key
        key = key[:len(cipher_text)] # Extracting the key of size same as the plain text
        
        print("Decrypted text: ",decryption(cipher_text,key))
        
    elif(len(key) > len(cipher_text)):
        print("Key length should match the length of the plain text!")
        
#%%