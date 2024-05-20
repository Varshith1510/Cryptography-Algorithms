# Playfair cipher
import string
import numpy as np

letters = list(string.ascii_lowercase)

key = input("Enter the key: ").lower()
key_chars = list(key)

plain_text = input("Enter a string: ").lower()
plain_chars = list(plain_text)

# Remove whitespaces in the text
for char in plain_chars:
    if char == ' ':
        plain_chars.remove(char)

matrix_sequence = []
l = ['i','j']

# First enter the key chars
for char in key_chars:
    if char not in matrix_sequence:
        if char == 'i' or char == 'j':
            if l not in matrix_sequence:
                matrix_sequence.append(l)
        else:
            matrix_sequence.append(char)
    
# Next fill the remaining chars 
for char in letters:
    if char not in matrix_sequence:
        if char == 'i' or char == 'j':
            if l not in matrix_sequence:
                matrix_sequence.append(l)
        else:
            matrix_sequence.append(char)

# Representing the matrix_sequence as a 5*5 matrix
matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(matrix_sequence[j])
    matrix_sequence = matrix_sequence[j+1:]
    matrix.append(row)

# Displaying the 5 * 5 matrix
print("\nMatrix Representation: ")
for row in matrix:
    for char in row:
        print(char,end=" ")
    print()
    
# Creating digrpahs(i.e. splitting the text into sequence of 2)
def create_digraph(plain_chars):
    digraphs = []
    
    for i in range(100):
        # If no of plain chars is odd, then add a filler char
        if len(plain_chars) == 1:
            plain_chars.append('z')
        chars = list(plain_chars[:2]) # First 2 chars
        
        # If both chars are same, then add a filler char
        if chars[0] == chars[1]:
            chars = [chars[0],'x']
            plain_chars = plain_chars[1:]
            # If no of plain chars is odd, then add a filler char
            if (len(plain_chars)%2 == 1):
               plain_chars.append('z')
        else:
            plain_chars = plain_chars[2:]
        
        digraphs.append(chars)
        if (len(plain_chars) == 0):
            break
    
    print("\nDigraphs obtained: ",digraphs)
    
    return digraphs
    
# Creating a char index mapping
char_idx = {}

char_array = np.array(matrix,dtype=object)
for idx,char in np.ndenumerate(char_array):
    if char == l:
        char_idx[char[0]] = idx
        char_idx[char[1]] = idx
    else:
        char_idx[char] = idx   
        
dict_keys = list(char_idx.keys())
dict_vals = list(char_idx.values()) 
       
# Encryption


def encryption(digrpahs):
    cipher_text = ''
    
    for pair in digraphs:
        
        c1,c2 = pair[0],pair[1]
        # Find index of both chars
        c1_idx,c2_idx = char_idx[c1],char_idx[c2]
        print(f"\nplain char 1: {c1} - {c1_idx}\nplain char 2: {c2} - {c2_idx}")
        # Check if they belong to same column (i.e. if the 2nd number of the index is same)
        if c1_idx[1] == c2_idx[1]:
        # Take the char below it (i.e. increment the row number)
            cipher_c1_pos = dict_vals.index(tuple(((c1_idx[0] + 1)%5, c1_idx[1])))
            cipher_c2_pos = dict_vals.index(tuple(((c2_idx[0] + 1)%5, c2_idx[1])))
            
            # Find the cipher chars
            cipher_c1 = dict_keys[cipher_c1_pos]
            cipher_c2 = dict_keys[cipher_c2_pos]
            
        # Check if they belong to the same row (i.e. if the 1st number of the index is same)
        elif c1_idx[0] == c2_idx[0]:
            # Take the char to the right of the current char(i.e. increment the column number)
            cipher_c1_pos = dict_vals.index(tuple((c1_idx[0], (c1_idx[1] + 1) % 5)))
            cipher_c2_pos = dict_vals.index(tuple((c2_idx[0], (c2_idx[1] + 1) % 5)))
            
            # Find the cipher chars
            cipher_c1 = dict_keys[cipher_c1_pos]
            cipher_c2 = dict_keys[cipher_c2_pos]
          
        # If the chars lie at differnt cols or rows
        else:
            # Form a rectangle using the chars & also the letters that are at the horizontal opposite corner of the rectangle
            # i.e. Only the column no is interchanged between the chars
            cipher_c1_pos = dict_vals.index(tuple((c1_idx[0],c2_idx[1])))
            cipher_c2_pos = dict_vals.index(tuple((c2_idx[0],c1_idx[1])))
            
            # Find the cipher chars
            cipher_c1 = dict_keys[cipher_c1_pos]
            cipher_c2 = dict_keys[cipher_c2_pos]
            
        print(f"\ncipher char 1: {cipher_c1}\ncipher char 2: {cipher_c2}")
        
        cipher_text += cipher_c1
        cipher_text += cipher_c2
    
    return cipher_text
    
digraphs = create_digraph(plain_chars)
cipher_text = encryption(digraphs)
print("\nCipher text: ",cipher_text)

# Decryption

cipher_chars = list(cipher_text)
    
def decryption(digrpahs):
    plain_text = ''
    
    for pair in digraphs:
        
        c1,c2 = pair[0],pair[1]
        # Find index of both chars
        c1_idx,c2_idx = char_idx[c1],char_idx[c2]
        print(f"\nplain char 1: {c1} - {c1_idx}\nplain char 2: {c2} - {c2_idx}")
        # Check if they belong to same column (i.e. if the 2nd number of the index is same)
        if c1_idx[1] == c2_idx[1]:
        # Take the char above it (i.e. decrement the row number)
            plain_c1_pos = dict_vals.index(tuple(((c1_idx[0] - 1)%5, c1_idx[1])))
            plain_c2_pos = dict_vals.index(tuple(((c2_idx[0] - 1)%5, c2_idx[1])))
            
            # Find the plain chars
            plain_c1 = dict_keys[plain_c1_pos]
            plain_c2 = dict_keys[plain_c2_pos]
            
        # Check if they belong to the same row (i.e. if the 1st number of the index is same)
        elif c1_idx[0] == c2_idx[0]:
            # Take the char to the left of the current char(i.e. decrement the column number)
            plain_c1_pos = dict_vals.index(tuple((c1_idx[0], (c1_idx[1] - 1) % 5)))
            plain_c2_pos = dict_vals.index(tuple((c2_idx[0], (c2_idx[1] - 1) % 5)))
            
            # Find the plain chars
            plain_c1 = dict_keys[plain_c1_pos]
            plain_c2 = dict_keys[plain_c2_pos]
          
        # If the chars lie at differnt cols or rows
        else:
            # Form a rectangle using the chars & also the letters that are at the horizontal opposite corner of the rectangle
            # i.e. Only the column no is interchanged between the chars
            plain_c1_pos = dict_vals.index(tuple((c1_idx[0],c2_idx[1])))
            plain_c2_pos = dict_vals.index(tuple((c2_idx[0],c1_idx[1])))
            
            # Find the cipher chars
            plain_c1 = dict_keys[plain_c1_pos]
            plain_c2 = dict_keys[plain_c2_pos]
            
        print(f"\nplain char 1: {plain_c1}\nplain char 2: {plain_c2}")
        
        plain_text += plain_c1
        plain_text += plain_c2
    
    return plain_text

digraphs = create_digraph(cipher_chars)
plain_text = list(decryption(digraphs))

while (plain_text[-1] == 'z'):
    plain_text.remove('z')

print("\nPlain text: ",''.join(plain_text))
