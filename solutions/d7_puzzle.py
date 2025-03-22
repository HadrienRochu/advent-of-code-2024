
DAY_NUMBER = 7

def parsing_puzzle():

    with open(f"d{DAY_NUMBER}_puzzle_input.txt", 'r') as file:
        data = file.read().splitlines()
    return data


def main1():
    pass

if __name__ == "__main__":
    puzzle_input_path = f"d{DAY_NUMBER}_puzzle_input.txt"
    # puzzle_input = 'd6_fake_puzzle_input.txt'
    main1(puzzle_input_path)