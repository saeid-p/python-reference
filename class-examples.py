# Python has no real concept of private elements.


class MyClass(object):
    """This is a test class."""

    # Every method, included in the class definition passes the object in question as its first parameter.
    # The word 'self' is used for this parameter (usage of self is actually by convention).
    def __init__(self, prop1=None):
        """Default class initializer"""
        self.prop1 = prop1

    def getProp1(self):
        return self.prop1

    def setProp1(self, value):
        self.prop1 = value

    @property
    def prop2(self):
        """A profoundly important string."""
        return self._prop2

    @prop2.setter
    def prop2(self, value):
        self._prop2 = value

    def myFunc(self, param1):
        """This is a test function."""
        print(param1)


class MyDerivedClass(MyClass):
    def extraMethod():
        print("Child Class!")


instance1 = MyClass()
instance1.myFunc("Message")
print(instance1.getProp1())
instance1.prop2 = "String!"

instance2 = MyDerivedClass("First Value")
print(instance2.getProp1())
instance2.setProp1("New Value")
print(instance2.getProp1())

# Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes,
# including methods. This is known as the Method Resolution Order (MRO).
# As as a result, it supports multiple inheritance.
