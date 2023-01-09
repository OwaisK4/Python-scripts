from kwargs import variadic_add

if __name__=="__main__":
    a = [1,2,3]
    b = [1,2,3]
    c = [1,2,3]
    d = list(map(variadic_add, a, b, c))
    print(d)
    e = list(filter(lambda x: x % 2 != 0, a))
    print(e)
    # a[len(a):] = range(4,10)
    # print(a)