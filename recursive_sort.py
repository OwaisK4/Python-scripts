from random import sample

def InsertionSort(num : list) -> list:
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] > key:
            num[j+1] = num[j]
            j = j - 1
        num[j+1] = key
    return num

class Sorting:
    numbers = []
    def __init__(self, arr : list):
        self.numbers = arr
    def recursiveSort(self, i = 0):
        if numbers == []:
            return
        a = max(numbers)
        numbers.remove(a)
        self.recursiveSort(a)
        numbers.append(a)
        
    

if __name__ == "__main__":
    # numbers = [randint(0, 20) for i in range(10)]
    """
    numbers = []
    while len(numbers) < 10:
        a = randint(0, 20)
        if a not in numbers:
            numbers.append(a)
    """
    numbers = sample(range(20), 10)
    s = Sorting(numbers)
    print(s.numbers)
    s.recursiveSort()
    # s.numbers = InsertionSort(s.numbers)
    print(s.numbers)