import pwd
import hashlib
import getpass

def login():
    username = input('Enter your username: ')
    try:
        user_info = pwd.getpwnam(username)
        crypted_passwd = user_info.sp_pwdp
        if crypted_passwd == 'x' or crypted_passwd == '*':
            raise ValueError('No support for shadow passwords')
        cleartext = getpass.getpass('Enter your password: ')
        return hashlib.crypt(cleartext, crypted_passwd) == crypted_passwd
    except KeyError:
        print('User not found.')
        return False
if login():
    print('Login successful!')
else:
    print('Incorrect username or password.')




 

import itertools
import string

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return f'Password is {guess}. Found in {attempts} guesses.'
print(guess_password('abc'))






class PasswordCracker:
    def __init__(self):
        pass
    def login(self, username, password):
        try:
            user_info = pwd.getpwnam(username)
            crypted_passwd = user_info.sp_pwdp
            if crypted_passwd == 'x' or crypted_passwd == '*':
                raise ValueError('No support for shadow passwords')
            return hashlib.crypt(password, crypted_passwd) == crypted_passwd
        except KeyError:
            return False
    def bruteforce_passwords(self, password_list):
        for password in password_list:
            result = self.guess_password(password)
            if result:
                return result
        return 'Password not found.'
    def guess_password(self, real):
        chars = string.ascii_lowercase + string.digits
        attempts = 0
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=password_length):
                attempts += 1
                guess = ''.join(guess)
                if guess == real:
                    return f'Password is {guess}. Found in {attempts} guesses.'
# Example usage:
if __name__ == '__main__':
    cracker = PasswordCracker()
    potential_passwords = ['password123', 'letmein', 'admin']
    print(cracker.bruteforce_passwords(potential_passwords))