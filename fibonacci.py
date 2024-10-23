import sys

def fibonacci(n):
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = int(sys.stdin.read().strip())

    print(" ".join(str(num) for num in fibonacci(n)))