#w4rm15h
#2/6/21
#password keeper

#__import__ 
import os
from termcolor import colored as c
from cryptography.fernet import Fernet

#Settings for this shitttt.....
class settings():
    colour = "green"

class vars():
    new_entry = []

#Getting the entry data
def getting_information():
    nickname = input("Profile nickname\n: ")
    email_address = input("Enter the email address\n: ")
    password = input("Enter the password\n: ")
    notes = input("Any other notes you want to add...\n: ")
    os.system('clear')
    print(c('--------------', f'{settings.colour}'))
    print('Entry Created!')
    print(c('--------------', f'{settings.colour}'))
    print(f"Profile Nickname: {nickname}")
    print(f"Email Address: {email_address}")
    print(f"Password: {password}")
    print(f"Other Notes\n{notes}")
    print("Do you want to save?")
    ctn = input("y/n").lower()
    if ctn == 'y' or 'yes':
        print("YYYYYYYYYYYYY")
    else:
        print('NAHHHHHHHHHHH')


if __name__ == "__main__":
    getting_information()













random_crap = '''

from cryptography.fernet import Fernet
  
# we will be encryting the below string.
message = "hello geeks"
  
# generate a key for encryptio and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key
  
key = Fernet.generate_key()
  
# Instance the Fernet class with the key
  
fernet = Fernet(key)
  
# then use the Fernet class instance 
# to encrypt the string string must must 
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
  
print("original string: ", message)
print("encrypted string: ", encMessage)
  
# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methos
decMessage = fernet.decrypt(encMessage).decode()
  
print("decrypted string: ", decMessage)

'''