import string
import numpy as np

letters = list(string.ascii_lowercase)

# Character index mapping
char_idx = {}

for i in range(len(letters)):
    char_idx[letters[i]] = i
    
dict_keys = list(char_idx.keys()) # Contains letters
dict_vals = list(char_idx.values()) # Contains numbers

    
plain_text = input("Enter a string: ").lower()
plain_chars = list(plain_text)

# Remove whitespaces in the text
for char in plain_chars:
    if char == ' ':
        plain_chars.remove(char)
        
# Key is a square matrix
key_size = 2
key_elements = [int(i) for i in input("Enter 4 elements of the key matrix: ").split(' ')]

key_matrix = np.array(key_elements).reshape((key_size,key_size))

print("\nKey matrix:\n",key_matrix)

def create_digraph(text_chars):
    digraphs = []
    
    for i in range(100):
        # If no of plain chars is odd, then add a filler char
        if len(text_chars) == 1:
            text_chars.append('z')
        chars = list(text_chars[:2]) # First 2 chars
        
        # If both chars are same, then add a filler char
        if chars[0] == chars[1]:
            chars = [chars[0],'x']
            text_chars = text_chars[1:]
            # If no of plain chars is odd, then add a filler char
            if (len(text_chars)%2 == 1):
               text_chars.append('z')
        else:
            text_chars = text_chars[2:]
        
        digraphs.append(chars)
        if (len(text_chars) == 0):
            break
    
    print("\nDigraphs obtained: ",digraphs)
    
    return digraphs
    
plain_digraphs = create_digraph(plain_chars)

def encryption(digraphs,key_matrix):
    
    cipher_text = ''
    
    for pair in digraphs:
        # Find the corresponding index of each char
        c1,c2 = pair[0],pair[1]
        c1_idx,c2_idx = char_idx[c1],char_idx[c2]
        print(f"\nplain char: {c1} - {c1_idx}\nplain char: {c2} - {c2_idx}")
        # Convert the numbers into a matrix
        char_matrix = np.array([c1_idx,c2_idx]).reshape(2,1)
        
        # Perform matrix multiplication with key matrix
        cipher_idx = ((np.matmul(key_matrix,char_matrix))%26).tolist()
        
        # Finding the new chars
        cipher_c1 = dict_keys[cipher_idx[0][0]]
        cipher_c2 = dict_keys[cipher_idx[1][0]]
        
        print(f"\ncipher char: {cipher_c1} - {cipher_idx[0][0]}\ncipher char: {cipher_c2} - {cipher_idx[1][0]}")
        
        cipher_text += cipher_c1
        cipher_text += cipher_c2
        
    return cipher_text

# Decryption process
cipher_text = encryption(plain_digraphs, key_matrix)
print("\nCipher text: ",cipher_text)

# Creating digraphs of the cipher text
cipher_chars = list(cipher_text)
cipher_digraphs = create_digraph(cipher_chars)

# Finding the inverse of the key
def key_inverse(key_matrix):
    # inv(A) = (1/det(A)) * adj(A)
    
    # Finding the determinant of the matrix
    det = int(np.linalg.det(key_matrix))

    # If det < 0 perform repeated addition until det > 0 then apply mod 26
    while det < 0:
        det += 26
    det = det % 26 # If det > 26
        
    print("\nDeterminant of Key matrix: ",det)
    
    # Finding the adjoint of the key matrix
    adj = np.zeros(shape=(2,2))
    adj[0][0] = key_matrix[1][1]
    adj[1][1] = key_matrix[0][0]
    adj[0][1] = -(key_matrix[0][1])
    adj[1][0] = -(key_matrix[1][0])

    # Check if any value in the adjoint matrix < 0
    
    for i in range(key_size):
        for j in range(key_size):
            while(adj[i][j] < 0):
                adj[i][j] += 26
            adj[i][j] = (adj[i][j])%26 # If that particular cell value > 26

    print("\nAdjoint of key matrix:\n",adj)
    
    if det == 1:
        print("\nInverse of key matrix: ",adj)
        return adj
        
    else:
        # Find the multiplicative inverse of (1/det(A))
        mul_inverse = 0
        # Condition - (det(A) * x) % 26 = 1, find x
        for num in range(1,27):
            if ((det * num)%26 == 1):
                mul_inverse = num
                break
        print(f"\nMultiplicative inverse of {det}: ",mul_inverse)
        
        for i in range(key_size):
            for j in range(key_size):
                adj[i][j] = ((adj[i][j]) * mul_inverse) % 26
                
        print("\nInverse of key matrix:\n",adj)
        return adj

def decrytpion(cipher_digraphs,key_inv):
    
    plain_text = ''
    
    for pair in cipher_digraphs:
        # Find the corresponding index of each char
        c1,c2 = pair[0],pair[1]
        c1_idx,c2_idx = char_idx[c1],char_idx[c2]
        print(f"\ncipher char: {c1} - {c1_idx}\ncipher char: {c2} - {c2_idx}")
        # Convert the numbers into a matrix
        char_matrix = np.array([c1_idx,c2_idx]).reshape(2,1)
        
        # Perform matrix multiplication with key matrix
        plain_idx = ((np.matmul(key_inv,char_matrix))%26).tolist()
        
        # Finding the new chars
        plain_c1 = dict_keys[int(plain_idx[0][0])]
        plain_c2 = dict_keys[int(plain_idx[1][0])]
        
        print(f"\nplain char: {plain_c1} - {int(plain_idx[0][0])}\nplain char: {plain_c2} - {int(plain_idx[1][0])}")
        
        plain_text += plain_c1
        plain_text += plain_c2
        
    return plain_text
        
key_inv = key_inverse(key_matrix) 
print("\nPlain text: ",decrytpion(cipher_digraphs, key_inv))
 
#%%

# Alternate way to find adjoint of a matrix
arr = np.array([[3,3],[2,5]])
det = np.linalg.det(arr)
inv = np.linalg.inv(arr)
print(inv)
adj = inv * det

for i in range(2):
    for j in range(2):
        while (adj[i][j] < 0):
            adj[i][j] += 26
            
print(adj)