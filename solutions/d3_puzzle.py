import re

def parsing_puzzle3():
    """
    OUTPUT format:
        list[list[int]]: list of list of integers
    """
    parsed_data = []
    with open('d3_puzzle_input.txt', 'r') as file:
        data = file.read().splitlines()
    return data

def get_mul(line:str)->list:
    regex = re.compile('mul\(\d{1,3}\,\d{1,3}\)')
    return regex.findall(line)

def multiply(mul:str)->int:
    factors = mul[4:-1].split(',')
    return int(factors[0]) * int(factors[1])

def main1():
    data = parsing_puzzle3()
    list_mul = []
    for line in data:
        list_mul += get_mul(line)
    puzzle_solution = 0
    for mul in list_mul:
        puzzle_solution += multiply(mul)
    print(f"day 3 - puzzle 1 solution: {puzzle_solution}")


def get_enable(line:str)->str:
    regex = re.compile("(?<=do\(\)).*?(?=don't\(\))")
    return "#####".join(regex.findall("do()"+line+"don't()"))



def main2():
    data = parsing_puzzle3()
    all_in_data = "#".join(data)
    enabled:str = get_enable(all_in_data)
    list_mul = get_mul(enabled)
    puzzle_solution = 0
    for mul in list_mul:
        puzzle_solution += multiply(mul)
    print(f"day 3 - puzzle 2 solution: {puzzle_solution}")

if __name__ == '__main__':
    # main1()
    main2()