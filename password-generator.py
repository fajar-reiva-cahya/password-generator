# Code By Fajar Reiva Cahya

import random
import string

def generate_password(length):
    if length < 6:
        print("Panjang Password Harus 6 Karakter !")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator\n")
    length = int(input("Masukan Panjang Karakter Password Yang Diinginkan: "))
    password = generate_password(length)
    
    if password:
        print(f"Password Yang Telah Di Buat : {password}")

if __name__ == "__main__":
    main()
