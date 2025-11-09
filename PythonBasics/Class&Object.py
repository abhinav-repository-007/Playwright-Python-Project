# This program is about OOPs Class n Objects
# Class is a user defined blueprint or prototype. It is a collection of attributes(variables) + methods(function)
# An Object is an instance of a class.

class Calculator:
    num = 100               # Class variable

    def getData(self):      # Class method
        print("I am executing as class method.")

obj = Calculator()
obj.getData()
print("{}{}".format("I am a class variable = ", obj.num))
print("I am added just to see whether, update code pushed to Remote repo.")
print("This is to avoid merge")

