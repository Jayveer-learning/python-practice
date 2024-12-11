from cryptography.fernet import Fernet
import message_data
import os 
# Generate key for encremption or decreption 

key = Fernet.generate_key()

# create instance of class Frenet to use all methods and properties 
# easliy 
cipher = Fernet(key)


message_Is = message_data.message

with open("message_key_data.key", "wb") as key_file:
    key_file.write(key)

# encrypte data 
encrypted_data = cipher.encrypt(message_Is.encode())
print(encrypted_data)

with open("encyrepted_message.txt", "wb") as encyrepted_message:
    encyrepted_message.write(encrypted_data)
    print("Success fully done!")

# decrypte_data
decrypte_data = cipher.decrypt(encrypted_data.decode())
print(decrypte_data)

