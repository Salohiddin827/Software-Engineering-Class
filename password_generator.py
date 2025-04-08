import random
import string

print("Welcome to the Password Generator!")
nr_uppercase_letters = int(input("How many uppercase letters would you like to have in your password?\n"))
nr_lowercase_letters = int(input("How many lowercase letters would you like to have in your password?\n"))
nr_symbols = int(input("How many symbols would you like to have?\n"))
nr_numbers = int(input("How many numbers would you like to have?\n"))

lowercase_letters = random.choices(string.ascii_lowercase, k=nr_lowercase_letters) 
uppercase_letters =  random.choices(string.ascii_uppercase, k=nr_uppercase_letters) 
numbers = random.choices(string.digits, k=nr_numbers)
symbols = random.choices(string.punctuation, k = nr_symbols)


password_list = []

for _ in range(nr_uppercase_letters):
    password_list.append(random.choice(uppercase_letters))

for _ in range(nr_lowercase_letters):
    password_list.append(random.choice(lowercase_letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)
print(f"Your password is: {password} ")
