# about Scope
username = 'anubhav'
def func():
    username = 'sumit' # this is only in functional Scope
    print(username) # -> sumit

print(username) # -> anubhav
func()





# ---------------- Closures --------------------

x = 99
def calculate(num):
    def func(x):
        return x ** num
    return func # --------> this is just returning a function defination

a = calculate(2)
b = calculate(3) # ----> num = 3
 
print(a(3)) # 3**2 == 3 ^ 2 = 9 = ans
print(b(5)) # -----> this is just calling of func(5) which is function defination return by calculate(3) => ans = 5**num = 5**3 = 5^3 = 125