def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs")
        return func(*args, **kwargs)

    return wrapper # returning function defination not calling it


@debug
def hello():
    print("Hola!!!")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", "namaste")
