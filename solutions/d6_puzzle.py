from d6_grid import Grid
from d6_guard import Guard



def construct_grid(file_path:str)->Grid:
    with open(file_path, 'r') as f:
        grid = [list(line) for line in f]
    fake_grid = [
        '..#..',
        '....#',
        '..^..',
        '#....',
        '...#.',
    ]
    # return Grid(fake_grid)
    return Grid(grid)

def construct_guard(grid:Grid)->Guard:
    return Guard(grid)

def move_until_end(guard:Guard)->int:
    while guard.move():
        pass
    return guard.count_visited()

def rotate_right(direction:tuple[int, int])->tuple[int, int]:
    return (direction[1], -direction[0])

def count_possible_obstructions(guard:Guard, grid:Grid)->int:
    # return sum([1 for x, y, direction in guard.visited if (x, y, rotate_right(direction=direction)) in guard.visited and grid.is_valid_location_for_obstacle(x=x+direction[0], y=y+direction[1]) ])
    count = 0
    for x, y, direction in guard.visited[1:]:
        if (x, y, rotate_right(direction=direction)) in guard.visited[1:] and grid.is_valid_location_for_obstacle(x=x+direction[0], y=y+direction[1]):
            print(f"Possible obstruction at: {x+direction[0], y+direction[1]}")
            count += 1
    return count


def main1(puzzle_input:str):
    grid = construct_grid(puzzle_input)
    guard = construct_guard(grid)
    puzzle_solution1 = move_until_end(guard)
    print(f"puzzle dimensions: {grid.dim}")
    # print("printing grid:")
    # grid.print_grid()
    print(f"day 6 - puzzle 1 solution: {puzzle_solution1}")

    puzzle_solution2 = count_possible_obstructions(guard=guard, grid=grid)
    print(f"day 6 - puzzle 2 solution: {puzzle_solution2}")


if __name__ == "__main__":
    puzzle_input = 'd6_puzzle_input.txt'
    # puzzle_input = 'd6_fake_puzzle_input.txt'
    main1(puzzle_input)