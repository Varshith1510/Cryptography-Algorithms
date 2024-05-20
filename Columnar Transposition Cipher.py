import string
import math

letters = list(string.ascii_lowercase)

print("Welcome to Columnar Transposition Cipher!\nWhat operation would you like to perform?\n\n1. Encryption\n2. Decryption")
choice = int(input("Enter your choice: "))

if (choice == 1): # i.e. Encryption
    plain_text = input("Enter a string: ").lower()
    key = input("Enter the key: ").lower()
    
    cols = len(key) # Key size denotes the no of columns in the matrix
    rows = math.ceil(len(plain_text)/len(key)) # Empty cells should be filled with filler char(say *)
    
    plain_chars = list(plain_text)
    plain_chars_copy = plain_chars.copy()
    key_chars = list(key)
    sorted_key = sorted(key_chars)
    
    # To add filler chars
    filler_count = len(key) - (len(plain_text) % len(key))
    
    if filler_count != 0:
        filler_char = list('*' * filler_count)
        plain_chars.extend(filler_char)
        plain_chars_copy = plain_chars.copy()
    
    sorted_idx = {}
    for i in range(len(sorted_key)):
        sorted_idx[sorted_key[i]] = i+1
        
    print("\nMatrix Representation:\n")
    # Displaying the key chars
    for char in key_chars:
        print(char,end=" ")
    print()
    # Displaying the order
    for char in key_chars:
        print(sorted_idx[char],end=" " )
    print("\n")
    
    matrix = []
    # Filling the matrix
    for i in range(rows):
        row = [] # Characters that will enter into each row of the matrix
        for j in range(cols):
            row.append(plain_chars_copy[j])
        plain_chars_copy = plain_chars_copy[cols:]
        matrix.append(row)

    # Displaying the matrix
    for row in matrix:
        for char in row:
            print(char,end = " ")
        print()
    
    # Finding the cipher text
    cipher_text = ''
    
    for char in sorted_idx.keys():
        key_idx = key_chars.index(char) # Represents the column to extract
        for row in range(rows): # Going through each row of that particular column
            cipher_text += matrix[row][key_idx]
            
    print("\nCipher Text: ",cipher_text)
    
    
if (choice == 2): # i.e. Decryption
    cipher_text = input("Enter a string: ").lower()
    key = input("Enter the key: ").lower()
    
    cols = len(key) # Key size denotes the no of columns in the matrix
    rows = math.ceil(len(cipher_text)/len(key)) # Empty cells should be filled with filler char(say *)
    
    cipher_chars = list(cipher_text)
    
    key_chars = list(key)
    initial_key_idx = {}
    for i in range(len(key_chars)):
        initial_key_idx[key_chars[i]] = i+1 
    
    sorted_key = sorted(key_chars)
    sorted_idx = {}
    for i in range(len(sorted_key)):
        sorted_idx[sorted_key[i]] = i+1
        
    print("\nMatrix Representation:\n")
    # Displaying the key chars
    for char in key_chars:
        print(char,end=" ")
    print()
    # Displaying the order
    sorted_ord = [] # Contains the position(col) in which the character is supposed to be placed 
    for char in key_chars:
        print(sorted_idx[char],end=" " )
        sorted_ord.append(sorted_idx[char])
    print("\n")
    
    matrix = [] # Will contain lists that will be entered column wise
    # No of entries per column = No of rows
    # Break the cipher text into row characters
    for i in range(cols): 
        col = []
        for j in range(rows):
            col.append(cipher_chars[j])
        col.append(initial_key_idx[key_chars]) # Sort the matrix based on this number
        cipher_chars = cipher_chars[rows:]
        matrix.append(col)
    print(matrix)
    # Sort the columns in the matrix based on the numbering of the key chars
    # i.e h(3) -> 3rd list in the matrix should come under h
    def number(l):
        '''Takes a list that contains characters with a number at the end'''
        return l[-1]
    sorted_matrix = sorted(matrix,key=number)
    print(sorted_matrix)
    plain_text = []
    
    # Extracting the plain text from the matrix
    for row in range(rows):
        for col in (sorted_matrix): # Iterating through the inner lists inside the matrix
        # No of entries in each list depends on the number of rows
            plain_text.append(col[row])

    plain_copy = plain_text.copy()            
    
    # Displaying the text in the matrix form
    for i in range(rows):
        for j in range(cols):
            print(plain_copy[j],end=" ")
        plain_copy = plain_copy[cols:]
        print()
                    
    
    # Displaying the plain text
    while(plain_text[-1] == '*'): # Removing the filler chars
        plain_text.remove('*')
    
    print("\nPlain text: ",''.join(plain_text))
    
    
    
    
    
        
    
    
    
    
    
    