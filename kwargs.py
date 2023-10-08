def func(date, *paper, **student):
    print(f"Today's date is: {date}.")
    print(f"Paper: ", end="")
    for args in paper:
        print(args, end=" ")
    print(f"\nStudent:")
    for kwargs in student:
        print(f"{kwargs}: {student[kwargs]}")

def variadic_add(*args : int) -> int:
    sum: int = 0
    for arg in args:
        sum += arg
    return sum

if __name__=="__main__":
    a = variadic_add(1,2,3,4,5)
    print(a)
    s = lambda x,y: x + y
    print(s(1,5))
    # func("26 Nov 2022", "COAL THEORY", "EE-2003", Name="Owais Ali Khan", Section="3-F", Roll_no="21K-3298")