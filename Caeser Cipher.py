import string

letters = list(string.ascii_letters[:26]) # Extracting only lowercase letters

chars = dict() # Creating a dictionary that holds the char:num mapping

# Mapping process
for i in range(len(letters)): 
    chars[letters[i]] = i+1

def encryption(plain_text,shift):
    ''' Takes a string and a num as input. Returns a cipher text by shifting each character forward by the num specified'''
    cipher_txt = ''
    
    for i in plain_text:
        new_char_idx = (chars[i]+shift) % 26 # Identifying the position of new char in the dictionary
        new_char = letters[new_char_idx - 1] # Assigning the new char
        cipher_txt += new_char
        
    return cipher_txt
    
        
def decryption(cipher_text,shift):
    ''' Takes a string and a num as input. Returns a cipher text by shifting each character backward by the num specified'''
    plain_txt = ''
    
    for i in cipher_text:
        new_char_idx = (chars[i] - shift) % 26
        new_char = letters[new_char_idx - 1]
        plain_txt += new_char
        
    return plain_txt

print("Welcome to Caeser Cipher!\nWhat operation would you like to perform?\n\n1.Encryption\n2.Decryption")
choice = int(input("Enter your choice: "))

if (choice == 1):
    plain_text = input("Enter a string: ").lower()
    shift = int(input("Enter the shift value: "))
    print("Cipher Text: ",encryption(plain_text,shift))
    
elif (choice == 2):
    cipher_text = input("Enter a string: ").lower()
    shift = int(input("Enter the shift value: "))
    print("Plain Text: ",decryption(cipher_text,shift))
    



