# This program is about Inheritance
# Calculator class from Constructor.py will act as Parent class here.
from Constructor import Calculator          # from file_name import class_name


class Child(Calculator):                # Child inherit properties of Parent(Calculator) class
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 20, 20)       # If Parent Constructor have code then need to call, if default, then no need.


    def total(self):
        print("I am a Child method.")
        return self.num + self.firstNum + self.secondNum + self.num2        # 100 + 20 + 20 + 200

obj = Child()
print(obj.total())

