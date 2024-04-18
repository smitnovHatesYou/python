import random;

password_length = input("How long would you like your password to be?:  ")

password_length = int(password_length)

include_lowercase = input("Include lowercase letters? (y/n): ")

include_uppercase = input("Include uppercase letters? (y/n): ")

include_numbers = input("Include numbers? (y/n): ")

include_specials = input("Include special characters? (y/n): ")


lowercase = 'abcdefghijklmnopqrstuvwxyz'

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = '0123456789'

specials = '!@#$%^&*()'
    

character_set = ''
if include_lowercase == "y":
    character_set += lowercase
if include_uppercase == "y":
    character_set += uppercase
if include_numbers == "y":
    character_set += numbers
if include_specials == "y":
    character_set += specials


password = ''.join(random.choices(character_set, k=password_length))

print(password)