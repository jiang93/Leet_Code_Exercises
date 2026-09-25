class Accumulator:

    def __init__(self) -> None:
        # private attribute
        self.__count = 0

    # access private attribute using @property and @count.setter decorators
    # count = property(count)
    @property
    def count(self) -> int:
        return self.__count

    """
    # setter method
    # count = count.setter(count)
    @count.setter
    def count(self, value: int) -> None:
        self.__count = value
    """
    # normal add method
    def add(self, more: int = 1) -> None:
        self.__count += more

"""
accum = Accumulator()
accum.count = 3
"""