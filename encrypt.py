from crypto import password_encrypt

def encrypt():
    message = input("Enter message to encrypt: ")
    password = input("Enter a password: ")
    repeated_password = input("Repeate your password: ")

    if password != repeated_password:
        print("ERROR: Passwords don't match")
        return
    
    encrypted = password_encrypt(message=message, password=password)
    
    print(encrypted)

if __name__ == "__main__":
    encrypt()