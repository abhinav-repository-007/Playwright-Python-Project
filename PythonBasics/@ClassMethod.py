class MyClass:

    @classmethod
    def class_method(cls):
        return "I am Class method, not require obj to call, just annotate me with @classmethod, arg should be cls, access with class name"

    def instance_method(self):
        return "I am a normal method inside class, hence require obj creation, n access me with object name"

obj = MyClass()
print(MyClass.class_method())
print(obj.instance_method())
