class MyClass:
    a = 0
    s = "Owais"
    def f(self):
        print("Hello World")

if __name__ == "__main__":
    print(MyClass.s)
    MyClass.f(MyClass())
    MyClass.counter = 1
    while MyClass.counter < 10:
        MyClass.counter *= 2
    print(MyClass.counter)
    del MyClass.counter