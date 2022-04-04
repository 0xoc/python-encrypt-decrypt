from crypto import password_decrypt

def decrypt():
    message = input("Enter Encrypted Message: ")
    password = input("Enter a password: ")    
    encrypted = password_decrypt(token=message, password=password)
    print(encrypted)

if __name__ == "__main__":
    decrypt()