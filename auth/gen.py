import itertools
import string
import time
import win32security
 
def brute_force_cracker(target_pass):

    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    start_time = time.time()

    # Test lengths starting from 1 up to a reasonable limit
    for length in range(1, 9): 
        # product() generates every possible combination with replacement
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            
            if guess == target_pass:
                duration = time.time() - start_time
                return guess, attempts, duration
    return None

def verify_windows_password(username, password): 
    try:
        # This attempts a local interactive logon  
        token = win32security.LogonUser(
            username,
            None, # Local machine
            password, 
            win32security.LOGON32_LOGON_INTERACTIVE,
            win32security.LOGON32_PROVIDER_DEFAULT 
        )
        return True
    except Exception as e: 
        # Error 1326 is "Logon failure: unknown user name or bad password" 
        return False

target = verify_windows_password()
result = brute_force_cracker(target)
if result:
    print(f"Success! Password: {result[0]}")
    print(f"Attempts: {result[1]} | Time: {result[2]:.2f}s") 
