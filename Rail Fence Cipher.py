import string
import numpy as np

letters = list(string.ascii_lowercase)

plain_text = input('Enter a string: ').lower()
plain_chars = list(plain_text)

allocated_chars = plain_chars.copy() # To keep track of all the characters that are stored in the matrix

rail = int(input('Select the no of rails: '))

# Construct a matrix based on the length of plain text & the no of rails
# Rows = no of rails  &  Cols = len(plain text)
total_cells = len(plain_text) * rail
filler = list('*' * total_cells)

matrix = np.array(filler,dtype = 'object').reshape((rail,len(plain_text)))

# Filling the characters in zig zag fashion
# Encryption
row = 0
check = 0
for i in range(len(plain_chars)):
    if check == 0:
        matrix[row][i] = plain_chars[i]
        row += 1
        if row == rail:
            check = 1
            row -= 1
            # inner if
    elif check == 1:
        row -= 1
        matrix[row][i] = plain_chars[i]
        if row == 0:
            check = 0
            row = 1
    
print(matrix)

cipher_text = ''

for i in range(rail):
    for j in range(len(plain_chars)):
        if matrix[i][j] != '*':
            cipher_text += matrix[i][j]
            
print("Cipher text: ",cipher_text)

cipher_chars = list(cipher_text)

# Decryption
# To perform decryption, first we need to mark where the characters should be placed

# Mark the matrix in zig zag fashion
cipher_matrix = np.array(filler,dtype='object').reshape(rail,len(cipher_text))       

# Traversing the matrix in zig zag fashion

row = 0
check = 0
for i in range(len(cipher_chars)):
    if check == 0:
        cipher_matrix[row][i] = '_'
        row += 1
        if row == rail:
            check = 1
            row -= 1
            
    elif check == 1:
        row -= 1
        cipher_matrix[row][i] = '_'
        if row == 0:
            check = 0
            row = 1
            
# Fill characters in the marked positions

for i in range(rail):
    for j in range(len(cipher_chars)):
        if cipher_matrix[i][j] == '_':
            cipher_matrix[i][j] = plain_chars[j]

print(cipher_matrix)  

# Now traverse in zig zag fashion to extract the original text      
original_text = ''

row = 0
check = 0

for i in range(len(cipher_chars)):
    if check == 0:
        original_text += cipher_matrix[row][i]
        row += 1
        if row == rail:
            check = 1
            row -= 1
            
    elif check == 1:
        row -= 1
        original_text += cipher_matrix[row][i]
        if row == 0:
            check = 0
            row = 1
            
print("Original text: ",original_text)