import copy

from typing import List


class Stack:
    """
    Class of Stack.
    Stack is a list of element where:
    - only last element added can be acessed
    - elemen can be added only at the end
    """

    def __init__(self, values: List[int]):
        self.values = values
        self.length = len(values)

    def pop(self) -> int:
        """remove and return the last element of the Stack

        Raises:
            BufferError: occur when trying to pop an empty stack

        Returns:
            int: last element of the Stack
        """
        if self.length == 0:
            raise BufferError("The stack object is empty")
        else:
            self.length -= 1
            return self.values.pop()

    def add(self, e: int):
        """add element on the top of the Stack

        Args:
            e (int): element to be added
        """
        self.values.append(e)
        self.length += 1

    def __deepcopy__(self, memo=None):
        """rewrite deepcopy method.
        The goal is to clone an existing stack.

        Args:
            memo (_type_, optional): Memo is the dictionary that is
                                    used by the `deepcopy` library to prevent infinite recursive copies in
                                    instances of circular references. Pass it to all the `deepcopy` calls
                                    you make in the `__deepcopy__` implementation to prevent infinite
                                    recursions.
                                    Defaults to None.

        Returns:
            _type_: cloned stack
        """

        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        deepcopied_values = copy.deepcopy(self.values, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(deepcopied_values)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new