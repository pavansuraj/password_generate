import random

def generate_password(pw_length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pw_length:
        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    return passwords

def replace_with_number(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword

def replace_with_uppercase_letter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")
    password_lengths = []
    print("Minimum length of password should be 3")
    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i + 1}: "))
        if length < 3:
            length = 3
        password_lengths.append(length)
    generated_passwords = generate_password(password_lengths)
    for i, password in enumerate(generated_passwords):
        print(f"Password #{i + 1} = {password}")
        
if __name__ == "__main__":
    main()
