"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """ Make a new serial number from start  """
        self.start =  self.next = start

    def __repr__(self):
        """  show representation  """
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """ Take the starting serial and add 1 each time it is called  """
        self.next += 1
        return self.next - 1

    def reset(self):
        """  Resets serial counter to original number """
        self.next = self.start

serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
print(serial.generate())
print(serial.generate())


