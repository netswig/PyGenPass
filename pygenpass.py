import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("PyGenPass!")
nr_letters = int(input("Number of letters:\n> "))
nr_symbols = int(input(f"Number of symbols:\n> "))
nr_numbers = int(input(f"Number of integers:\n> "))

password_list = []
password = ""
for x in range(0, nr_letters):
    new_char = random.choice(letters)
    password_list.append(str(new_char))

for x in range(0, nr_symbols):
    new_char = random.choice(symbols)
    password_list.append(str(new_char))

for x in range(0, nr_numbers):
    new_char = random.choice(numbers)
    password_list.append(str(new_char))

random.shuffle(password_list)
password.join(password_list)

for x in password_list:
    password = password + x

print(f"\n\nPassword: {password}\n\n")