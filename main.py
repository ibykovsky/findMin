from time import sleep

# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.

def func(x):
    return (x-1.5)**2

def findMin(a,b,eps,f):

    def printout(a,b,x,fa,fb,fx):
        print(f"a={a:18}\tx={x:18}\tb={b:18}")
        print(f"{fa:18}\t\t{fx:18}\t\t{fb:18}")

    fa = f(a)
    fb = f(b)
    x = (a+b)/2
    fx = (x)

    while 1:
        printout(a,b,x,fa,fb,fx)

        if(fa>fb):
            if(abs(fx-fb)<eps):
                return x
            else:
                a = x
        else:
            if(abs(fx-fa)<eps):
                return x
            else:
                b = x
        fa = f(a)
        fb = f(b)
        x = (a+b)/2
        fx = (x)

        sleep(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(f"result = {findMin(-2,2,1e-6,func)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
