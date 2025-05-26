x = 99
def calculate(num):
    def func(x):
        return x ** num
    return func

a = calculate(2)
b = calculate(3)

print(a(3))
print(b(3))