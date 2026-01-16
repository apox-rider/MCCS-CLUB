import time
def password_Checker():
    while True:
        password = input("Enter a password : ")
        if len(password.strip())>=8:
            time.sleep(2)
            print("Password length confirmed ")
            time.sleep(2)
            print("Checking if password has number ...")
            hasNumber=any(char.isdigit() for char in password)
            if hasNumber==True:
                time.sleep(2)
                print("Password valid")
            else:
                print("Password Invalid. Password should have atleast one number")
        else:
            print("Password Invalid. Length unsatisfactory")


print("Welcome to the password validator!!")
time.sleep(3)
password_Checker()

