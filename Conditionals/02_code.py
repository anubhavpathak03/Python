import random

class_marks = random.randint(0, 100)

def checking(number):
    if number > 90:
        print("Your marks is: ", class_marks, "\nSecure A Grade. Excellent Job!!!")
    elif number > 80:
        print("Your marks is: ", class_marks, "\nSecure B Grade. Good Job!!!")
    elif number > 70:
        print("Your marks is: ", class_marks, "\nSecure C Grade. Good!!!")
    else:
        print("You Can Do it. Keep It Up!!!")

checking(class_marks)
