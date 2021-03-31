import sys
import random
import string


# of course, you can make a password generator in one line of code,
# but here I am giving an example of how functions can achieve a similar effect
# import random, string
# password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(10)])
# print(password)


password = []
characters_left = -1


def update_characters_left(number_of_characters):
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print(f"No valid character {characters_left}")
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print(f"Character remaining: {characters_left}")


password_length = int(input("How long your password should be? "))

if password_length < 5:
    print("Password must have minimum 5 letters")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("How many small letters? "))
update_characters_left(lowercase_letters)
uppercase_letters = int(input("How many uppercase letters? "))
update_characters_left(uppercase_letters)
special_characters = int(input("How many special characters? "))
update_characters_left(special_characters)
digits = int(input("How many digits? "))
update_characters_left(digits)

if characters_left > 0:
    print("No all characters are used. The password will be completed with lowercase letters.")
    lowercase_letters += characters_left

print()
print(f"Password lenght: {password_length}")
print(f"Lowercase letters: {lowercase_letters}")
print(f"Uppercase letters: {uppercase_letters}")
print(f"Special characters: {special_characters}")
print(f"Digits: {digits}")

for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Generated Password: ", "".join(password))
