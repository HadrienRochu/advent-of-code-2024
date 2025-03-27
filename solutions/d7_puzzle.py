from d7_Equation import Equation
import datetime

DAY_NUMBER = 7


def read_puzzle():

    with open(f"./input/d{DAY_NUMBER}_puzzle_input.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()
    return data


def parsed_line(line: str):
    line_splitted = line.split(":")
    result = int(line_splitted[0])
    terms = line_splitted[1].split(" ")[1:]
    terms = list(map(int, terms))
    return result, terms


def main1():
    data = read_puzzle()

    _sum = 0
    for line in data:
        result, values = parsed_line(line)
        equation = Equation(result, values[::-1])
        _sum += result if equation.resolve_equation(stack=equation.stack) else 0
    print(f"day {DAY_NUMBER} - puzzle 1 solution: {_sum}")


def main2():
    t0 = datetime.datetime.now()
    data = read_puzzle()

    _sum = 0
    for line in data:
        result, values = parsed_line(line)

        # equation_without_concat = Equation(result, values[::-1], operators=["+", "*"])
        # _sum += (
        #     result
        #     if equation_without_concat.resolve_equation(
        #         stack=equation_without_concat.stack
        #     )
        #     else 0
        # )

        equation_with_concat = Equation(
            result, values[::-1], operators=["+", "*", "||"]
        )
        _sum += (
            result
            if equation_with_concat.resolve_equation(stack=equation_with_concat.stack)
            else 0
        )
    t1 = datetime.datetime.now()
    print(f"day {DAY_NUMBER} - puzzle 2 solution: {_sum}")
    print(f"Computation time : {t1 - t0}")


if __name__ == "__main__":
    # main1()
    main2()
