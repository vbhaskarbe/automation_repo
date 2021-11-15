class OurClass(object):
    """Class docstring."""

    def __init__(self, arg1, arg2):
        """Method docstring."""
        self.arg1 = arg1
        self.arg2 = arg2

    def printargs(self):
        """Method docstring."""
        print self.arg1
        print self.arg2


instance = OurClass('arg1', 'arg2')
print type(instance)
instance.printargs()
print dir(instance)
