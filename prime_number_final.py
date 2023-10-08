def prime(num : int) -> int:
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(f"{i} ", end="")
    return None

if __name__ == "__main__":
    n = 11
    prime(n)
    