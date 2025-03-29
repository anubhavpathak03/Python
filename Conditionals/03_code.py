import random
import string

digits = random.choices(string.digits + string.ascii_letters, k=random.randint(0, 10))

password = ''.join(digits)

if len(password) >= 10:
    print("Your Password is Strong.")
elif len(password) > 6:
    print("Your Password is Good")
else:
    print("Your Password is Week")