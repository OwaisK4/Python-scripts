from sys import argv

def square(function : callable):
    def wrapper(num : int):
        f = function(num)
        for i in range(len(f)):
            f[i] = f[i] * f[i]
        return f
    return wrapper

@square
def createList(num : int) -> list[int]:
    if num < 0:
        raise ValueError("Num must be nonnegative integer.")
    l = [i for i in range(1, int(num) + 1)]
    return l

if len(argv) > 1:
    num : int  = argv[1]
else:
    num : int  = 5
print(createList(num))