
def capitalize(func : str):
    def wrapper(string):
        a : str = func(string)
        a.upper()
        print(a)
    return wrapper

@capitalize
def func(string):
    print(string)

func("Hello World")