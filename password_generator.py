import random

lowc_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          ]
upc_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_up_letters = int(input("How many uppercase letters would you like to have in your password?\n"))
nr_low_letters = int(input("How many lowercase letters would you like to have in your password?\n"))
nr_symbols = int(input("How many symbols would you like to have?\n"))
nr_numbers = int(input("How many numbers would you like to have?\n"))

password_list = []

for _ in range(nr_up_letters):
    password_list.append(random.choice(upc_letters))

for _ in range(nr_low_letters):
    password_list.append(random.choice(lowc_letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)
print(f"Your password is: {password} ")
