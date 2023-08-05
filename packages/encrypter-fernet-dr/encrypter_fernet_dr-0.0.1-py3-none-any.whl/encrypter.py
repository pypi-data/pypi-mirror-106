from cryptography.fernet import Fernet

def encrypt_file(file, key_file=None):
    '''Creates an encrypted copy of a file using Fernet (symmetric encryption) in the working directory.
    The function takes a file as main argument and a key_file as optional argument. If no key_file
    is given, then a key for the encryption is created using Fernet.generate_key()'''

    if key_file != None:
        with open(key_file, 'rb') as filekey:
            key = filekey.read()
    else:
        key = Fernet.generate_key() # key generation
        key_file = 'my_key.key'

        # string the key in a file
        with open(key_file, 'wb') as filekey:
            filekey.write(key)

    fernet = Fernet(key) # using the generated key

    # opening the original file to encrypt
    with open(file, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    file_name = str(file.name)+'_encrypted'

    # opening the file in write mode and writing the encrypted data
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return (file_name, key_file)

def decrypt_file(encrypted_file, key):
    ## using the key
    with open(key, 'r') as key_file:
        my_key = key_file.read()
    fernet = Fernet(my_key)

    # opening the encrypted file
    with open(encrypted_file, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    decrypted_file_name = str(encrypted_file+'_decrypted')
    with open(decrypted_file_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    return decrypted_file_name

