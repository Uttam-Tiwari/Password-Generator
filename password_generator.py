import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1,2,3,4,5,6,7,8,9,0]

symbols = [
     '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '~', '`', '§', '¶', '©', '®', '™', '°', 'µ', '¿',
    '¢', '£', '¥', '€', '¤', '†', '‡', '•', '∞', '÷'

    ]

print("Welcome to Password generator!")

user_letter=int(input("How many letters you want in your password?:\n"))

user_number = int(input("How many numbers you want in your password?:\n"))

user_symbol = int(input("How many symbols you want in your password?:\n"))

password_list = []

for i in range(1,user_letter+1):
    character = random.choice(letters)
    password_list += character

for j in range(1,user_number+1):
    num = random.choice(numbers)
    password_list += str(num)

for k in range(1,user_symbol+1):
    sym = random.choice(symbols)
    password_list += sym

random.shuffle(password_list)

password = ''

for char in password_list:
    password += char
    
print("Your password is:",password)
