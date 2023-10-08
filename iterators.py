import sys

class Reverse_using_iterator_class:
    """Iterator class for reversing a string."""
    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def Reverse_using_generator(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

if __name__ == "__main__":
    # print("Hello World")
    # string = input("Enter a string to reverse: ")
    if len(sys.argv) > 1:
        string = sys.argv[1]
    else:
        string = "owais"
    r = Reverse_using_iterator_class(string)
    for i in r:
        print(i, end="")
    print()
    r = Reverse_using_generator(string)
    for i in r:
        print(i, end="")