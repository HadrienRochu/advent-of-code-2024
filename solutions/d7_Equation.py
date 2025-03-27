import copy

from typing import List

from d7_stack import Stack


class Equation:

    result: int
    stack: Stack

    def __init__(
        self, result: int, values: List[int], operators: list[str] = ["+", "*"]
    ):
        self.stack = Stack(values)
        self.result = result
        self.operators = operators

    def resolve_equation(self, stack: Stack) -> bool:
        if stack.length == 0:
            return False
        elif stack.length == 1:
            return stack.pop() == self.result
        else:
            e0 = stack.pop()
            e1 = stack.pop()

            # easy test to simplify branchs
            if e0 > self.result:
                return False

            # operator ||
            if "||" in self.operators:
                concat_stack = copy.deepcopy(stack)
                concat_stack.add(int(str(e0) + str(e1)))
                resolved_bool = self.resolve_equation(concat_stack)
                if resolved_bool:
                    return resolved_bool

            # operator *
            if "*" in self.operators:
                product_stack = copy.deepcopy(stack)
                product_stack.add(e0 * e1)
                resolved_bool = self.resolve_equation(product_stack)
                if resolved_bool:
                    return resolved_bool

            # operator +
            if "+" in self.operators:
                stack.add(e0 + e1)
                return self.resolve_equation(stack)
