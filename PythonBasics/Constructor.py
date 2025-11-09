# This program is about Constructor
# Self is keyword mandatory for calling the class variables / instance variables

class Calculator:
    num = 100                       # Variable declared in Class is Class Variable

    # Default Constructor : def _init__(self):
    # below not default, it has code, means have some meaning
    def __init__(self, a, b):             # Constructor declaration. Always __init__ in Python.
        self.firstNum = a                          # Variable declared in Constructor is Instance Variable
        self.secondNum = b
        print("I am executed automatically when object is created. I am used to initialize object.")

    def getData(self):
        print("I am executing as class method.")

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num             # Class var can be called with class name or self.

obj1 = Calculator(10, 20)
obj1.getData()
print(obj1.num)
addition = obj1.summation()
print("Sum = ", addition)

obj2 = Calculator(30, 40)
obj2.getData()
print(obj2.num)
addition = obj1.summation()
print("Sum = ", addition)

obj1 = Calculator(50, 60)               # Using same object multiple times, no need to create seperate obj everytime
addition = obj1.summation()
print("Sum = ", addition)

