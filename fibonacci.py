import sys

def fibonacci(n):
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    if sys.version_info[0] < 3: #Check Python version on system
        n = int(raw_input("Enter the max number for the Fibonacci Series: ")) #Python2
    else:
        n = int(input("Enter the max number for the Fibonacci Series: ")) #Python3

    print("Fibonacci Series: " + " ".join(str(num) for num in fibonacci(n)))