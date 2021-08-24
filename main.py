from math import sin
from time import sleep


# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


def func(x):
    # return (x-1.5)**2
    return (x) ** 3 + x**2


def findMin(a, b, eps, f):
    def printout(x, fx, fn, dx):
        print(f"{x:18}\t\t{dx:18}\t\t{fx:18}\t\t{fn:18}")

    x = (a + b) / 2
    dx = abs((a - b) / 4)

    while 1:

        fx = f(x)
        xn = x + dx

        if xn < a or xn > b:
            return (x, fx)

        fn = f(xn)
        df = fn - fx

        printout(x, fx, fn, dx)

        if abs(df) > eps:
            if (df > 0):
                dx = -dx / 3
            x = xn
        else:
            return (x, fx) if fx < fn else (xn, fn)

        # sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(f"result = {findMin(-10, 10, 1e-9, func)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
