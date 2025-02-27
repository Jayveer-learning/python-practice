# Cryptography

from cryptography.fernet import Fernet

# 1. Generate a key and write it to a file (key must be 
# secerely stored)

key = Fernet.generate_key()
cipher = Fernet(key) # ->  # `cipher` refers to the encryption instanc

# save key to file for later use  and [use wb for writing only binary file]
with open("secret.key", "wb") as key_file:
    key_file.write(key)


data = "this is a secret message"

# 2. Encrypt some data (convert data to bytes)
encrypted_data = cipher.encrypt(data.encode())
# encrypted_data = Fernet(key).encrypt(data.encode()) #-> do this 
# if you can't create any instance of Fernet

print(f"Encrypted : {encrypted_data}")
# encrypted data :- YMU8nYONDldXDl0LmKHh-3kGfyhRSYpUhL-59CyodrfywIOg='



# 3. Decrypt the encrypted data using the same key
decrypted_data = cipher.decrypt(encrypted_data.decode())
print(f"Decrypted: {decrypted_data}") #-> decrypted data :- Decrypted: this is a secret message




# key = Fernet.generate_key()  # This creates a random key
# cipher = Fernet(key)  # Here, you create the `cipher` instance

#     Fernet.generate_key():
#         This generates a random key (a sequence of bytes) that is 32 bytes long and base64-encoded. This key will be used for both encrypting and decrypting data.
#         Think of this key like a special password that is needed to lock (encrypt) and unlock (decrypt) your secret message.
#     cipher = Fernet(key):
#         Here, you are creating an instance of the Fernet class and storing it in the variable cipher.
#         You need to pass the key (generated earlier) to the Fernet class because the Fernet instance (cipher) needs to know which key to use for encryption and decryption.
#         This instance, cipher, can now use that key to securely encrypt and decrypt data.

# Why the key is important:

#     Without the key, you wouldn’t be able to encrypt or decrypt anything. The Fernet instance (cipher) uses the key to perform encryption, and it will also need the same key to decrypt the data.

# Example Comparison:

# Imagine you have a lock and a key:

#     The key is like the key to a lock (generated by Fernet.generate_key()).
#     The cipher is like the lock itself (created by Fernet(key)).
#     Without the key, you can’t lock or unlock anything (just like you can’t encrypt or decrypt data without it).