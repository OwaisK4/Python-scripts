import os

if __name__ == "__main__":
    print(os.getcwd())
    print(os.listdir())
    print(list(i for i in os.walk(os.getcwd())))