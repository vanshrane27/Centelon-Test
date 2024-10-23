import sys

def reverse_number(n):
    return int(str(n)[::-1])

if __name__ == "__main__":
    n = int(sys.stdin.read().strip())

    print(reverse_number(n))