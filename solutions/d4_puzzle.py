from d4_puzzle_class import Puzzle4


def parsing_puzzle4():
    """
    OUTPUT format:
        list[list[int]]: list of list of integers
    """
    parsed_data = []
    with open('d4_puzzle_input.txt', 'r') as file:
        data = file.read().splitlines()
    return data

def main1():
    data = parsing_puzzle4()
    print(f"dim puzzle : {len(data)} lines x {len(data[0])} columns")
    puzzle = Puzzle4(data)
    puzzle_solution = 0
    for _ in range(4):
        puzzle_solution += puzzle.count(word='XMAS')
        puzzle.rotate_90()
    puzzle.rotate_45()
    for _ in range(4):
        puzzle_solution += puzzle.count(word='XMAS')
        puzzle.rotate_90()
    print(f"day 4 - puzzle 1 solution: {puzzle_solution}")


def debug():
    n = 5
    puzz_gen = [[str(i) + str(j) for j in range(n)] for i in range(0, n)]
    for l in puzz_gen:
        print(l)
    print()
    puzzle = Puzzle4(puzz_gen)
    puzzle.rotate_45()
    puzzle.rotate_90()
    # puzzle.rotate_90()
    # puzzle.rotate_90()
    # puzzle.rotate_90()
    for l in puzzle.matrix:
        print(l)

def main2():
    data = parsing_puzzle4()
    print(f"dim puzzle : {len(data)} lines x {len(data[0])} columns")
    puzzle = Puzzle4(data)
    puzzle_solution = puzzle.count_X_mas()
    print(f"day 4 - puzzle 2 solution: {puzzle_solution}")




if __name__ == '__main__':
    # debug()
    # main1()
    main2()