age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("senior citizen")


# using function

user_age = int(input("Tell me your age: \n"))

def checking(userage):
    if userage < 18:
        print("user not eligible for voting")
    else:
        print("user is eligible to vote")

checking(user_age)
