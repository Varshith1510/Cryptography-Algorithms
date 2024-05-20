import string

letters = list(string.ascii_letters[:26]) # Contains the set of all lowercase alphabets

chars = dict() # Dictionary for char - num mapping

# Creating the char-num mapping
for i in range(len(letters)):
    chars[letters[i]] = i


def encryption(text,key):
    cipher_text = ''
    
    # Split the word into individual characters using unpack(*) method
    plain_chars = [*text] 
    key_chars = [*key]

    # Since, we have to perform character wise addition
    combined = zip(plain_chars,key_chars) #Creates a zip object
    
    for pair in combined:
        # Find the index of new char
        new_idx = chars[pair[0]] + chars[pair[1]]
        if new_idx > 25:
            new_idx = new_idx - 26
        
        # Finding the cipher char
        new_char = letters[new_idx]
        cipher_text += new_char
    
    return cipher_text
    
    
def decryption(text,key):
    plain_text = ''
    
    # Split the word into individual characters using unpack(*) method
    cipher_chars = [*text] 
    key_chars = [*key]

    # Since, we have to perform character wise addition
    combined = zip(cipher_chars,key_chars) #Creates a zip object
    
    for pair in combined:
        # Find the index of new char
        new_idx = chars[pair[0]] - chars[pair[1]]
        if new_idx < 0:
            new_idx = new_idx + 26
        
        # Finding the cipher char
        new_char = letters[new_idx]
        plain_text += new_char
    
    return plain_text
    
print("Welcome to Vernam's Cipher!\nWhat operation would you like to perform?\n\n1. Encryption\n2. Decryption")
choice = int(input("Enter your choice: "))

if (choice == 1): # i.e. Encryption
    plain_text = input("Enter a string: ").lower()
    key = input("Enter a key: ").lower()
    
    # Plain text & key length should be the same
    if(len(key) < len(plain_text)): 
        extra_chars = len(plain_text) - len(key)
        key = key*extra_chars # Creating copies of the key
        key = key[:len(plain_text)] # Extracting the key of size same as the plain text
        print(key)
        print("Encrypted text: ",encryption(plain_text,key))
        
    if (len(key) > len(plain_text)):
        print("Key length should match the length of the plain text!")
        
        
if (choice == 2): # i.e. Decryption
    cipher_text = input("Enter a string: ").lower()
    key = input("Enter the key: ").lower()
    
    # Cipher text & key length should be the same
    if(len(key) < len(cipher_text)): 
        extra_chars = len(cipher_text) - len(key)
        key = key*extra_chars # Creating copies of the key
        key = key[:len(cipher_text)] # Extracting the key of size same as the plain text
        
        print("Decrypted text: ",decryption(cipher_text,key))
        
    if (len(key) > len(cipher_text)):
        print("Key length should match the length of the plain text!")
        
        
#%%
