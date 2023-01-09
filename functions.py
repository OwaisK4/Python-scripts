def fibonacci(a):
    if a == 0 or a == 1:
        return a
    return fibonacci(a-1) + fibonacci(a-2)
def gcd(n, k):
    if n == 0:
        return 0
    elif k == 1 or k == n:
        return 1
    return gcd(n-1, k) + gcd(n-1, k-1)

if __name__=="__main__":
    for i in range(1,11):
        # print(fibonacci(i), end=" ")
        print(gcd(10, i), end=" ")