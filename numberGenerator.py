from luhn import *
import sys
import math

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

def verifyLuhnInput(n):
    while verify(n) == False:
        while True:
            n = input("Please enter correct sim card number: ")
            try:
                int(n)
                break
            except ValueError:
                print("Please enter digits only.", file=sys.stderr)
    return n

while True:
    x = input("Enter first sim card number: ")
    try:
        int(x)
        break
    except ValueError:
        print("Please enter digits only.", file=sys.stderr)

x = verifyLuhnInput(x)
x = first_n_digits(int(x),len(x)-1)

while True:
    y = input("Enter last sim card number: ")
    try:
        int(y)
        break
    except ValueError:
        print("Please enter digits only.", file=sys.stderr)

y = verifyLuhnInput(y)
y = first_n_digits(int(y),len(y)-1)

if (x > y):
    print("First sim card number is greater than last sim card number. Please retry.")
else:
    count = y - x + 1
    while x <= y:
        print(append(str(x)))
        x += 1
    print("SIM card count:", count)
