import sys

def reverse_number(n):
    return int(str(n)[::-1])

if __name__ == "__main__":
    if sys.version_info[0] < 3: #Check Python version on the system
        n = int(raw_input("Enter a number: ")) #Python2
    else:
        n = int(input("Enter a number: ")) #Python3

    print("Number in Reverse Order:", reverse_number(n))