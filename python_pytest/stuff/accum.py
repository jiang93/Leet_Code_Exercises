class Accumulator:

    def __init__(self):
        # private attribute
        self.__count = 0

    def get_count(self) -> int:
        return self.__count
    count = property(get_count)

    def set_count(self, value: int) -> None:
        self.__count = value
    count = count.setter(set_count)

accumulator = Accumulator()
accumulator.count = 15
print(accumulator.count)

"""
    # access private attribute using @property decorator (getter method)
    @property
    def count(self) -> int:
        return self.__count
    
    # setter method
    @count.setter
    def count(self, value: int) -> int:
        self.__count = value

    # add method
    def add(self, more: int = 1) -> int:
        self.__count += more

accumulator = Accumulator()
accumulator.count = 15
print(accumulator.count)
accumulator.add(5)
print(accumulator.count)

"""
"""
    def get_count(self) -> int:
        return self.__count

    def set_count(self, value: int) -> int:
         self.__count = value

    count = property(get_count, set_count)

accumulator = Accumulator()
accumulator.count = 15
print(accumulator.count)
"""