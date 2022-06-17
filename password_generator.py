import random
import string

def create_password(psw_length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(characters, psw_length))
    return password

if __name__ == "__main__":
    print(create_password())