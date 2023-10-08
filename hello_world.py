if __name__ == "__main__":
    print("Hello World")
    a = 0
    b = 1
    l = list()
    while a < 10:
        print(a, end=" ")
        l.append(a)
        a, b = b, a+b
    print()
    # a = list(enumerate(range(10)))
    s = list(enumerate(l))
    print(s)
    s.clear()
    for i in range(2, 20):
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            s.append(i)
            # print(f'{i} is a prime number.')
    print(s)