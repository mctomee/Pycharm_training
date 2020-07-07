# Import the necessary libraries
from GCD import GCDCalc
import sys

# Define variables
a = None
b = None
fail = 1

# Request user input
print("Give me two integers")
while a is None:
    try:
        a = int(input("Value of A:"))
    except ValueError:
        fail += 1
        print("This is not an integer! Please give me the correct input")
        if fail > 5:
            print("Youhave failed more than 5 times. i do not want to waste my time")
            sys.exit()

while b is None:
    try:
        b = int(input("Value of B:"))
    except ValueError:
        fail += 1
        print("This is not an integer! Please give me the correct input")
        if fail > 6:
            print("Youhave failed more than 5 times. i do not want to waste my time")
            sys.exit()

print("Given value for (A) is :", a, ", and for (B) is:", b)

Calculator = GCDCalc(a, b)
print("The GDC of the given two numers is: ", Calculator.execute())
