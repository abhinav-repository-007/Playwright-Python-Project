# This program is about Functions
# Function : A function is a group of related statements to perform a specific task

def Greet():                    # Function declaration
    print("Hello")
Greet()                         # Function Call

def Greet1(name):               # Parameterized Function
    print("Hello " + name)
Greet1("Shivani")

def AddIntegers(a, b):
    return a + b
print("{}{}".format("Summation = ", AddIntegers(10, 5)))

